"""Read a single archived ima2 generation without contacting the provider."""

import argparse
import hashlib
import json
import sys
from pathlib import Path


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_optional(path):
    return read_json(path) if path.is_file() else {}


def file_sha256(path):
    with path.open("rb") as stream:
        digest = hashlib.sha256()
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def compare(expected, actual):
    if expected is None or actual is None:
        return "unverified"
    return "match" if expected == actual else "mismatch"


def find_job(manifest, job_id):
    with manifest.open(encoding="utf-8-sig") as stream:
        rows = [json.loads(line) for line in stream if line.strip()]
    matches = [row for row in rows if row.get("job_id") == job_id]
    if len(matches) != 1:
        raise ValueError(f"Expected one exact job ID match, found {len(matches)}")
    return matches[0]


def inspect(manifest, job_id, include_prompt):
    job = find_job(manifest, job_id)
    folder = manifest.parent / "job_logs" / job_id
    submission = read_optional(folder / "submission.json")
    receipt = read_optional(folder / "prompt_delivery_receipt.json")
    result = read_optional(folder / "result.json")
    provider_files = sorted(folder.glob("provider_metadata_*.json"))

    manifest_refs = job.get("refs") or []
    command = submission.get("command")
    sent_refs = None
    if isinstance(command, list):
        sent_refs = [value for flag, value in zip(command, command[1:]) if flag == "--ref"]
    ordered_refs = sent_refs if sent_refs is not None else manifest_refs

    prompt_path = Path(job["prompt_file"]) if job.get("prompt_file") else None
    source_exists = prompt_path is not None and prompt_path.is_file()
    source_check = compare(
        receipt.get("input", {}).get("source_sha256"),
        file_sha256(prompt_path) if source_exists else None,
    )

    generations = []
    receipt_by_name = {item.get("filename"): item for item in receipt.get("comparisons", [])}
    for provider_file in provider_files:
        provider = read_json(provider_file)
        filename = provider.get("filename")
        body_check = receipt_by_name.get(filename, {}).get("server_body_matches_expected_cli")
        generation = {
            "filename": filename,
            "server_prompt_matches_receipt": compare(True, body_check),
            "provider_ref_count_matches": compare(len(ordered_refs), provider.get("refsCount")),
        }
        if include_prompt:
            generation["server_user_prompt"] = provider.get("userPrompt")
        generations.append(generation)

    output_hashes = result.get("sha256") or {}
    outputs = []
    for name in result.get("outputs") or []:
        path = Path(name)
        present = path.is_file()
        outputs.append({
            "path": name,
            "present": present,
            "sha256_matches_result": compare(
                output_hashes.get(name), file_sha256(path) if present else None
            ),
        })

    report = {
        "job_id": job_id,
        "request_id": receipt.get("request_id"),
        "prompt_file": str(prompt_path) if prompt_path else None,
        "prompt_file_present": source_exists,
        "prompt_file_matches_receipt": source_check,
        "reference_order_source": "submission command" if sent_refs is not None else "job manifest",
        "reference_order_matches_manifest": compare(manifest_refs, sent_refs),
        "ordered_refs": [{"path": name, "present": Path(name).is_file()} for name in ordered_refs],
        "source_image": job.get("source_image"),
        "generations": generations,
        "outputs": outputs,
    }
    if include_prompt:
        report["archived_prompt"] = prompt_path.read_bytes().decode("utf-8-sig") if source_exists else None
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="Archived effective_jobs.jsonl or jobs.jsonl")
    parser.add_argument("job_id", help="Exact archived job ID")
    parser.add_argument("--summary", action="store_true", help="Omit prompt bodies from the report")
    args = parser.parse_args()
    if args.job_id in {".", ".."} or any(c in args.job_id for c in "/\\:"):
        parser.error("job ID must be a single name")
    try:
        report = inspect(args.manifest, args.job_id, include_prompt=not args.summary)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

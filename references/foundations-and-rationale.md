# 상세 원칙의 위치

v1.2에서 정리한 공통 원칙의 WHY와 예시를 이어받은 자료다. 공개판에서는 개인 사례의 경로·원고·세션 식별과 매체 전용 수치 목록을 제외했고, 원본 전문의 동일 바이트 복사라고 주장하지 않는다. 현재 `SKILL.md`와 사용자의 최신 결정이 우선한다. 직접적인 미적·상업적 목표, 작법 조사·체스터턴, 후보 탐색의 현재 기준은 v2.2 입구와 연결 참고문서를 따른다. 여기의 양식은 필요할 때 선택적으로 사용한다.

# Detailed Principles and Rationale

## Purpose

Use this skill as the **common baseline for image generation**.

It is not a style guide by itself. It defines how to translate a user's intent into a strong visual request, how to use references without letting them hijack the image, how to allocate limited visual complexity, how to preserve continuity, and how to review results without confusing technical completion with visual success.

A narrower character-specific skill, poster skill, webtoon skill, or project-local art direction may add stricter rules. Those narrower rules should override this baseline only where they are intentionally more specific.

---

## 1. Generation Intent Comes First

Do not silently cross from discussion, planning, critique, prompt-writing, or concept exploration into image generation.

Treat these as different phases:

- **discussion** — understand the idea, mood, story, or visual problem
- **prompt/design** — turn the idea into a concrete visual direction
- **generate** — create image candidates
- **edit** — modify a supplied or selected image
- **review** — compare the result against the intended visual effect

Generate only when the user has clearly asked to create, draw, generate, render, edit, or otherwise produce the image.

An explicit image-generation request is already permission to generate. Do not add redundant confirmation unless a missing fact would materially change the result.

When clarification is genuinely useful, ask only the smallest number of questions needed to get to a first useful image. If the user says “알아서”, “나머지는 알아서”, “you decide”, or equivalent wording, make the remaining creative choices yourself.

---

## 2. Find the Three-Axis Sweet Spot

The user's canonical three-axis wording is:

1. **내가 보여주고 싶은 것**
2. **이 이미지를 볼 때 제3자가 보고싶어할 것**
3. **상업적으로 보여줘야 할 것**

Treat these as the primary creative axes unless the user explicitly revises them. A broader assistant interpretation such as "what the image must show for its purpose" may be useful for a non-commercial task, but it must not silently replace the user's original third axis.

The target is the **sweet spot where all three overlap**. This is a creative judgment, not a scorecard and not a requirement that every visible element serve all three equally.

Ask internally:

- What do we most want to show?
- What would a third-party viewer actually want to keep looking at, discover, or feel?
- What must be commercially visible or compelling in this image?
- Where do those three demands reinforce one another instead of competing?

The three axes can operate at different scales. One may define the whole image, another the focal beat, and another the way the image earns attention or leaves the viewer wanting more.

Do not reduce the sweet spot to generic "make it appealing" language. Preserve the user's actual creative target and the reason the image is worth making.

---

## 3. Preserve Creative Context; Structure It Instead of Compressing It

For creative image work, **prompt brevity is not a quality goal**. Compression can destroy the information that lets a generative model understand why a scene works: creative WHY, causal context, emotional pressure, relationships, subtext, timing, adjacent beats, character knowledge, viewer knowledge, and the reason behind an art-direction choice.

Do not rewrite a rich approved creative brief into short keywords merely because it is long. If tens of thousands of characters are materially useful to the image, that length is acceptable.

Prefer **structured abundance** over lossy summarization. When the following affect staging, acting, interpretation, hierarchy, or viewer experience, actually carry them into the model-facing input rather than keeping them only in producer notes:

- the creator's WHY and intended reward
- relationship and emotional logic
- what each person knows, misunderstands, hides, expects, or notices
- causal links between the current moment and the preceding/following moment
- what the viewer already knows and what the image should let them discover
- approved prose instructions whose nuance affects the result
- examples that teach the model how to resolve competing demands
- exact identity/current-state reference roles
- exact visible text and ownership when text matters

Use headings, delimiters, role maps, authority labels, and explicit current-vs-legacy markers so a long prompt remains legible. **Structure is the optimization target; shortness is not.**

What may be compressed or omitted:

- duplicated operational logs
- stale rejected branches that no longer affect the current target
- tool/runtime chatter
- repeated file-management details
- debugging history whose lesson has already been converted into a clean current instruction
- genuinely redundant restatements

Do not replace a user-approved creative source or provider instruction with an assistant-authored summary unless the user explicitly asks for a summary or the source itself is being revised.

### When the current environment has input-length limits

Do not silently solve a length limit by deleting creative WHY or rewriting the source into a much shorter prompt. Use only mechanisms that the current environment actually supports, such as supported file attachment, reading a preserved resource in parts, or splitting context across supported inputs while keeping authority and ordering clear.

Do not assume that a particular local transport mode exists in this environment. If the actual model-facing input is not exposed, mark it as **unverified** rather than claiming that the complete source reached the image model.

A concise skill entrypoint and a long preserved creative resource are compatible: the skill can stay easy to discover while pointing to full case/source material when that material is relevant.

---

## 4. Separate Canonical Requirements From Creative Freedom

Every request should distinguish between what **must remain true** and what the image model may solve creatively.

### Must preserve

- identity and current version/state
- required subjects
- important relationships
- story- or concept-critical action
- exact product/prop facts
- exact visible text when required
- continuity-critical clothing or objects
- requested aspect ratio or output function
- any exact pose, gesture, crop, or physical relation that the user has made essential to this image

### Model may decide

- natural pose details that are not locked
- micro-expression when not critical
- exact crop when not locked
- lens/camera nuance when not locked
- small body shifts
- secondary lighting nuance
- nonessential background detail
- decorative texture

Do not turn art direction into a rigid micro-gesture checklist by default. But do not hide a genuinely critical pose or interaction inside vague freedom language either. If the user says a specific physical relation is the point of the image, lock it explicitly.

For expressive character work, a useful performance brief can include:

- outward impression
- hidden feeling or pressure
- relationship to the other subject
- what the pose/expression must read as
- what the model may choose freely

The aim is to give the model enough understanding to stage the image, while preserving the exact things the user actually cares about.

---

## 5. Use References by Role

References should have explicit jobs. Do not treat every attached image as a generic “make it like this” instruction.

Useful reference roles include:

- **identity reference** — face, body, character design, product identity
- **current outfit/state reference** — the specific version that should appear now
- **style reference** — rendering language, line quality, palette, texture
- **composition reference** — layout or camera logic only
- **setting reference** — architecture, environment, location cues
- **prop reference** — an important object whose form matters
- **continuity reference** — a previous approved/current image from the same scene
- **content proof** — evidence for factual appearance, signage, costume, object, etc.

Use the **minimum useful set of references**. More references are not automatically better.

Do not attach every available project image to every request. Irrelevant references consume attention and can contaminate identity, clothing, composition, or style.

When multiple references are attached, make the role map explicit in the prompt or working brief.

Example:

```text
REFERENCE ROLES
1. Character A — identity + current hairstyle
2. Character B — identity + current outfit
3. Station photo — setting cues only; do not copy people/composition
```

If the user already supplied references, prioritize them. When recognizable existing characters, places, products, or objects need better fidelity, gather a small number of clear official or otherwise reliable references when the workflow allows it.

---

## 6. Identity Is Not Composition

A character or object reference should usually stabilize **what the subject is**, not force the new image to reproduce the reference's pose, crop, camera, or background.

Similarly:

- a pose sheet does not imply multiple copies of the character
- a turnaround does not imply a neutral turnaround composition
- a style sheet does not define story staging
- a screenshot does not automatically become a literal screen layout
- a prior scene image used for continuity is not a command to paint over it

Tell the model what each reference contributes and what remains free.

---

## 7. Fresh Generation vs. Edit Must Be Explicit

When continuing a scene, decide which operation is intended:

### Fresh variation with continuity

Use the previous selected/current image as a **continuity reference**. Preserve relevant identity, environment, crowd, lighting, prop state, and scene language while creating a new composition or moment.

### Edit

Use the supplied image as the actual base and change only the requested region, object, text, style element, or other named target.

Do not accidentally turn a continuity request into a paint-over, or an edit request into an unrelated regeneration.

When an edit is requested, preserve unrequested content as much as the tool permits.

---

## 8. Treat Visual Complexity as a Budget

Use visual complexity as a practical production heuristic, not as a claim about a provider's hidden token accounting.

The useful operational idea is simple: **not every part of the image needs equal descriptive or rendered emphasis.** Deliberately decide where the viewer's attention and the model's expressive effort should go.

Spend more detail where it serves the current image, for example:

- faces and expressions
- hands when they carry action
- character interaction
- the key product or prop
- important text or UI
- the story-relevant environment cue
- the focal texture or material

Reduce or simplify elements that would compete without adding enough value, for example:

- incidental scenery
- decorative clutter
- background objects with no role
- meaningless labels/signage
- textures that fight the focal subject
- invented props that create continuity debt

This is **not** a universal command to leave backgrounds empty, make faces dominant, or use flat fields. A landscape, architectural image, environmental story, spectacle shot, product scene, or other image may legitimately spend most of its detail budget away from a face.

A visually quiet area can be a deliberate completed choice, but a richly rendered area can also be correct when the image's purpose requires it. The rule is hierarchy, not emptiness.

---

## 9. Give the Background a Job

Do not default to either “empty background” or “fully detailed background.” Decide what the background is doing for this image.

Useful background roles include:

- **flat / abstract** — strong subject isolation, icon-like presentation, graphic impact
- **simplified context** — enough cues to establish place or situation
- **information carrier** — screen, board, sign, map, interface, shelf, display
- **location-critical** — environment itself is a major subject, proof, reward, or story element
- **atmospheric** — light, weather, depth, color, or scale carries much of the mood
- **spectacle / world-building** — environmental richness is intentionally part of what the viewer came to see

When simplification is chosen, simplify the **attention demand**, not merely the number of named objects. A background can still feel noisy through dense patterns, tiny windows, excessive texture, repeated highlights, glitter, bokeh, fence grids, or micro-detail even when it contains only a few object categories.

When richness is chosen, make that richness purposeful. Do not let incidental detail compete with the intended focal hierarchy by accident.

---

## 10. Compose Around Relationships When the Image Is a Scene

For images built around interaction, action, or a lived moment, compose according to the actual relationships inside the scene:

- gaze toward actual partners or targets
- bodies toward conversation and action paths
- hands toward the objects they use
- usable surfaces of props toward their users
- motion according to the scene's physical logic

Natural side views, back views, partial occlusion, uneven spacing, foreground obstruction, and cropped bodies are valid when they serve the scene.

Direct eye contact with the viewer is appropriate when the image calls for direct address, portrait presentation, pin-up, selfie, interview, advertisement, confrontation, or another deliberate viewer-facing mode.

Do **not** elevate “the camera must have an in-scene narrative reason” into a universal law. Character sheets, fashion illustrations, promotional key art, product images, portraits, abstract images, and many pin-ups can use presentation-oriented cameras perfectly well.

The general rule is: choose the camera and body orientation that best serves the image's three-axis sweet spot, rather than inheriting one camera grammar for every kind of image.

---

## 11. Prefer Positive Construction Prompting

Describe the intended image as a **positive inventory** of what should exist and how it should work together.

Prefer:

```text
Two characters sit across a narrow table. Character A leans forward and watches Character B's hands. Character B avoids eye contact and folds a receipt. The café background is simplified to a window, table edge, and one hanging lamp so the hand action and tension dominate.
```

rather than a long defensive list of everything that must not happen.

Keep rejection reasons, failed-attempt analysis, and internal audit notes outside the provider prompt when possible.

Use negative instructions only for real blockers that repeatedly survive positive construction or when the user explicitly requests them.

---

## 12. Do Not Prompt the Internal Production Notes Into the Image

Separate **creative content** from **production cautions**.

Production notes may say things like:

- avoid confusing two reference roles
- previous attempt invented extra characters
- do not reuse an obsolete outfit
- a previous run misplaced text ownership

Those notes are useful for the assistant, but should not automatically be copied verbatim into the image request.

Translate them into clean positive instructions when possible:

```text
Visible cast: exactly Character A and Character B.
Character A uses reference 1; Character B uses reference 2.
Character A wears the attached winter coat version.
```

The model should receive the **resolved visual direction**, not the whole debugging history.

---

## 13. Exact Text Needs Ownership and Placement Logic

If readable text is important, do not provide a loose pile of phrases.

For each required string, know:

- exact wording
- language
- who or what owns it
- whether it is speech, caption, label, UI, sign, SFX, title, etc.
- intended reading order
- what object or character it belongs near

Example:

```text
VISIBLE TEXT
1. “괜찮아.” — Character A speech bubble, first
2. “진짜?” — Character B speech bubble, second
3. “OPEN” — door sign, background prop text
```

Speaker names are metadata, not text to render unless the user wants them visible.

Do not add decorative pseudo-text when the image does not need it. Random readable text becomes story information and can create errors or false meaning.

For very long or precision-critical text, consider a dedicated lettering/design pass when the available image workflow supports it.

---

## 14. Preserve Continuity Deliberately

Across a multi-image sequence, track only what actually needs to persist:

- character identity
- stable hairstyle or distinguishing features
- continuity-critical outfit
- prop state
- damage or transformation state
- weather/time-of-day when relevant
- room/stage geography
- crowd or companion presence
- camera language when the same scene continues

Do not create continuity debt casually. A conspicuous object, readable label, unusual accessory, or complex background introduced in one image may need to remain consistent later.

For same-scene continuation, reuse the best approved/current image as a continuity reference when useful.

For a new scene, do not carry old composition or background baggage just because a previous image exists.

---

## 15. Match Detail to Importance, Not to Empty Space

Do not fill space merely because space exists, and do not remove detail merely because simplicity is fashionable.

If the focal subject already communicates the image, surrounding space may stay simple. If environmental richness is itself the focal reward, give it the detail it needs.

If an emotionally important subject is too small to read, enlarge or crop it rather than spending more complexity elsewhere—unless distance itself is the intended effect.

When several demands compete, use the user's three-axis sweet spot to decide the order. A common fallback priority is:

1. the requested creative/commercial meaning
2. subject identity and required factual truth
3. key interaction/action or focal visual reward
4. required readable information
5. composition and hierarchy
6. continuity-critical elements
7. atmosphere and secondary detail
8. decorative richness

This order is a fallback, not a universal scorecard. The user may deliberately choose a different priority for a particular image.

---

## 16. Use Constraints as Ranges, Roles, and Priorities

Avoid unnecessary CAD-like micro-layout instructions.

Prefer:

- “upper third”
- “large foreground face”
- “small figure deep in the background”
- “quiet left side for title”
- “dense central cluster with simple edges”
- “wide breathing room around the product”

Use exact coordinates only when the task is genuinely layout-critical and the generation/editing tool can meaningfully obey them.

Percentages, ratios, and density numbers are best treated as **high-level expression budgets**, not pixel contracts.

---

## 17. First Useful Image Before Overengineering

Do not build unnecessary production machinery for a simple image request. This rule is about workflow overhead, not prompt length: a creatively rich request may still need a long prompt when its context materially improves the image.

An explicit request to generate, draw, render, or edit is already generation authorization. Do not insert another permission loop just because a reusable skill is active.

For an ordinary one-off image:

1. identify the three-axis sweet spot
2. identify the focal effect or reward
3. lock required subjects, identity, and any truly essential physical relation
4. choose only the references that materially help, with roles
5. decide composition/background hierarchy appropriate to this image type
6. carry the necessary WHY/context into the model-facing input
7. generate a first candidate
8. refine from the visible result and the user's judgment

Use a more formal packet only when complexity justifies it: multi-character continuity, exact branded objects, dense text, repeated series work, multi-image sequences, or production pipelines.

---

## 18. Review Against Intent, Not Merely Prompt Compliance

A generated file is not automatically a successful image.

Review in layers when review is requested or needed for the task.

### Objective

- correct subjects present
- identity recognizably preserved
- requested objects present
- text approximately/exactly correct when required
- dimensions/aspect appropriate
- no obvious reference-role contamination
- continuity preserved where required

### Visual / creative

- focal hierarchy matches the intended image
- expression/acting reads as intended when relevant
- relationships or presentation mode read correctly
- background/detail allocation supports the image rather than accidentally competing
- composition feels intentional
- the image delivers the requested creative/commercial effect

Technical PASS does not replace visual judgment. Successful attachment or file transport does not prove that the intended scene was actually reflected in the rendered image.

The user owns final aesthetic judgment and selection. When the user selects a candidate, record that selection as evidence that the **result was accepted for use**, not as proof that every source instruction was implemented successfully.

When the user asks for visual review, inspect the image and make concrete observations. Do not substitute hashes, dimensions, prompt presence, or generation completion for looking at the result.

---

## 19. Learn From Successes and Failures Without Polluting Future Prompts

When a result teaches a reusable lesson:

1. name what visibly worked or failed
2. identify the likely layer: intent, reference, prompt, composition, text, continuity, transport/runtime, or review workflow
3. preserve the evidence with an explicit status
4. update the smallest durable principle that prevents recurrence or protects the success
5. do not blindly paste the entire retrospective into every future prompt

Useful evidence labels include:

- `USER_SELECTED_SUCCESS` — the user chose the result for use
- `BENCHMARK_CANDIDATE` — useful comparison material, not yet a confirmed success authority
- `FAILURE_EXAMPLE` — must not be revived as a success precedent
- `EXPERIMENT_UNRESOLVED` — generated but not accepted/rejected conclusively

A user's selection proves selection. It does not automatically prove that every intended detail, hidden transport step, or source instruction succeeded.

A past failed output remains a **FAILURE_EXAMPLE**. Its availability in an archive does not make it a positive quality benchmark.

---

## 20. Separate Source, Actual Tool Input, Output, and Human Selection

Keep these stages distinct:

1. **source document** — the creative authority or approved source the producer intends to convey
2. **actual tool/model-facing prompt** — what the current image-generation tool actually received, if observable
3. **generated output** — what was actually rendered
4. **human selection/rejection** — what the user chose after seeing the result

Do not collapse them into one success state.

Examples of incorrect inference:

- source file attached successfully → therefore the model understood the scene
- source hash matched → therefore the final prompt preserved every important instruction
- output generated → therefore the art direction worked
- user selected the output → therefore every requested detail was implemented

If the current environment does not expose the exact model-facing prompt, say **actual model-facing input not verifiable**. Do not reconstruct a plausible prompt and present it as verified.

A real prior case showed that source/attachment integrity and actual scene transfer can diverge. Preserve this as a transport lesson, but do not assume that local transport behavior or command modes exist in the current platform.

---

# Default Image Brief

For a moderately complex generation request, construct the working brief from these fields:

```text
IMAGE GOAL
What the image should make the viewer notice / feel / understand:

OUTPUT FUNCTION
Where/how the image will be used; aspect ratio or format if important:

VISIBLE SUBJECTS
Exact cast / objects that should appear:

REFERENCE ROLE MAP
1. ... — identity / style / setting / prop / continuity / composition
2. ...

SCENE / ACTION / RELATIONSHIP
What is physically happening and how subjects relate:

COMPOSITION / CAMERA
Framing, hierarchy, gaze/body orientation, important empty areas:

STYLE / MEDIUM
Rendering language, era, material, photographic or illustrative behavior:

DETAIL BUDGET
What gets high detail; what stays quiet or simplified:

BACKGROUND ROLE
flat / simplified context / information carrier / location-critical / atmospheric:

CONTINUITY
What must match prior images, if anything:

VISIBLE TEXT
Exact strings + owner/channel/order, if any:

MUST PRESERVE
Non-negotiable identity, story, factual, or layout elements:

CREATIVE FREEDOM
What the model may decide naturally:
```

Use only the fields that matter for the task. Do not turn the template into bureaucracy.

---

# Provider-Prompt Structure Pattern

A useful provider prompt can use this shape when it fits the task. This is a structural pattern, not a target for brevity; long creative context may sit before, inside, or after these sections when it materially guides the image.

```text
Create [output type / medium] showing [subjects] while [scene/action].
The image should make the viewer first notice [focal effect].

Use the attached references as follows:
- [ref] for [identity/style/setting/etc.]

Compose the scene so [relationship/camera/hierarchy].
Spend visual detail on [focal features] and keep [secondary areas] simplified.
[Background role].

Preserve: [critical continuity / factual / text requirements].
Creative freedom: [pose/crop/lighting/secondary staging the model may decide].
```

The final provider prompt may be short or very long depending on the task. Preserve all creative context that materially changes interpretation, acting, staging, hierarchy, or reader experience. Remove only information that is operationally irrelevant, obsolete, or genuinely redundant.

---

# Relationship With Specialized Skills

This skill is the common layer and entrypoint. It should stay discoverable and procedural while allowing full source/context resources to remain intact when needed.

Examples:

- `Image Generation Principles` decides **how to preserve the user's three-axis creative intent, context, reference roles, hierarchy, transport evidence, and review boundaries**.
- a webtoon skill decides **page grammar, panel rhythm, text routing, white-manuscript behavior, and comic-specific density rules**.
- a project skill decides **canonical character designs, locations, recurring props, and current continuity**.

When a specialized skill provides a deliberate local rule, follow it for that task while retaining the general principles that do not conflict. Do not promote one successful project's numeric layout contract into a universal image default.

---

# One-Line Principle

**Start from the user's three axes — 내가 보여주고 싶은 것 / 이 이미지를 볼 때 제3자가 보고싶어할 것 / 상업적으로 보여줘야 할 것 — preserve the creative WHY and necessary context without lossy compression, distinguish must-preserve meaning from creative freedom, give references explicit roles, allocate visual complexity by the image's actual purpose, and judge the visible result separately from transport or technical completion.**

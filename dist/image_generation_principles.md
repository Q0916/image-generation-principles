# IGP v2.3 — Library 통합본

배포 조건: CC BY-NC 4.0 + 출처 표시 면제·상업적 제작 추가 허용. 출처 없이 사용·수정·무료 공유할 수 있고 유료 작업·결과물 판매도 허용한다. IGP 자체의 유료 재판매는 추가 허용 대상이 아니다. 표준 라이선스와 별도 허용문은 이 파일 끝에 수록했다.

2026-10-21. 이 파일을 읽고 현재 요청에 스킬처럼 적용한다. 저장만으로 모든 대화에 자동 적용된다고 가정하지 않는다. 본문은 기본 지침, 상세 원칙은 WHY가 필요할 때, 파편 셀채색은 요청된 경우만 읽는 미해결 실험이다. 실제 실행은 현재 도구와 사용자 요청의 범위를 따른다.

- 문서 1: Image Generation Principles (IGP)
- 문서 2: 일러스트 작법 조사·도메인 지식 적용·체스터턴의 울타리
- 문서 3: 제작 경험을 범용 이미지 연출로 재구성한 원칙
- 문서 4: 이미지 모델 입력·참조·후보 판정 패턴
- 문서 5: 상세 원칙의 위치
- 문서 6: 근거·가설·적용 범위
- 문서 7: 선택형 그림체 실험 — 파편화 셀채색 · 색점·망점


---

# 문서 1: Image Generation Principles (IGP)

# Image Generation Principles (IGP)

**버전:** 2.3 · 2026-10-21. 단독 이미지 작업의 기본 작화 판단 스킬이다. 사용자의 미적·상업적 목표, 실제 제작 경험과 작법 지식을 이미지 모델에 전달한다. 실행은 현재 사용 가능한 이미지 생성·편집 도구의 계약을 따른다.

**출발점과 현재 지위:** 사용자의 표현대로 “가설단계에서 이미지 모델에 생성협조를 요구한” 스킬이다. 작화 원리를 이해하고 구현을 요청하는 작업 가설·협업 지침이며, 모델의 내부 기제를 규명한 이론은 아니다. 좋은 실사용 결과에 대한 사용자 피드백은 있지만, 개별 조항의 인과 효과·보편적 재현성까지 검증된 것은 아니다. 적용 가설 → 실제 전달 → 출력 → 사용자 판단을 구별하며 결과로 개선한다. 근거와 적용 상태 (이 파일의 문서 6)를 참고한다.

**현재 확인 범위(2026-10-21): 긍정적인 실사용 피드백은 오로지 Codex에서 ima2로 이미지를 생성한 경로에서만 확인했다.** ima2는 여기서 실행 도구를 가리키며 정확한 내부 백엔드 모델 버전·전처리까지 검증했다는 뜻은 아니다. 공홈 Library에 파일을 추가하고 실제로 읽게 해 지침으로 적용할 수 있으며, Codex에서는 IGP와 ima2를 함께 사용할 수 있다. 이 사용 가능성과 모델별 효과 검증은 다르다. 다른 제공자에 대한 효과나 무작위 대조 실험으로 입증된 인과 효과는 주장하지 않는다.

## 언제 사용하고 언제 사용하지 않는가

- 사용: 이미지 아이디어 정리, 2D 그림체 설계, 그림 생성문 작성, 단일 이미지·일러스트·키비주얼 생성 또는 편집, 참조 이미지의 역할 분리, 후보 비교와 개선.
- 필요한 경우 적용: 여러 장이 같은 인물·의상·스타일을 공유하는 시리즈, 정보·대사·상업적 볼거리가 있는 시각물.
- 사용하지 않음: 사용자가 단순 감상·토론만 요청했는데 이미지 생성을 임의 실행할 때. **웹툰 전용 콘티·컷 시트·세로 합본 계약을 이 스킬로 대체할 때.** 현재 제공되지 않은 실행 도구나 전송 기능을 수행한 것처럼 말할 때.
- 좁은 매체·작품 스킬과 겹치면 그 작품이 정한 **형식·정확한 내용·정체성·현재 상태**를 따르고, 이 스킬은 충돌하지 않는 공통 연출 판단을 제공한다. 이미지 생성 도구·예산·상한은 현재 실제 환경과 사용자 요청이 결정한다.

## 1. 허용된 단계부터 시작한다

사용자 요청을 **구상 / 작화 방향·프롬프트 / 생성 / 특정 이미지 편집 / 시각 검토** 중 어디에 속하는지 파악한다. 구상만 요청되면 그림을 뽑지 않는다. 명시적 생성·편집 요청이면 다시 허락받기보다 실제 가능한 방법으로 진행한다. '알아서'라고 하면 안전한 범위의 표현 선택을 맡아 결정한다. 이미 사용자가 선택한 그림·글자·정체성·의미는 사용자 지시 없이 바꾸지 않는다.

## 1-1. 보고 싶은 것과 보여줄 곳을 최소한 확인한다

이미지의 구상·작화 방향·프롬프트·생성·편집을 시작하기 전에 다음 **두 가지가 사용자 요청이나 현재 대화에 명시되어 있는지 확인하고, 빠진 항목은 반드시 사용자에게 묻는다.** 둘 다 빠졌다면 한 번의 짧은 대화로 함께 묻는다.

1. **사용자가 그 일러스트에서 보고 싶은 것.** 예: “네가 이 일러스트에서 보고 싶은 건 뭐야?” 대상·장면·표정·몸의 선·분위기·그림체·미적 쾌감 등 사용자가 원하는 볼거리와 매력을 받는다. 에이전트 자신의 취향으로 대신 답하거나 서사적 명분·작법 용어를 요구하지 않는다.
2. **그림을 어디에, 누구에게 보여줄 것인지.** 예: “나만 볼 그림이야, 누군가에게 보여줄 그림이야? 게시한다면 어디에 올릴 거야?” 개인 감상인지, 특정인에게 보여줄 것인지, 커뮤니티·SNS·포트폴리오·판매 페이지 등에 게시할 것인지 확인한다. 개인 감상도 완결된 답이며 공개 게시를 전제로 몰아가지 않는다. 보여줄 상대나 게시처가 명시됐으면 필요한 만큼 그 맥락을 사용한다.

이 두 정보는 사용자가 원하는 보상과 관객이 마주할 맥락을 연결하기 위한 최소 조건이다. 같은 소재라도 혼자 즐기는 그림, 친구에게 보여주는 그림, 커뮤니티에 올리는 그림은 초점과 전달 방식이 달라질 수 있다. “예쁘게”, “귀엽게”, “야하게”도 첫 항목의 유효한 답이므로 그 요구를 정당화하게 하지 않는다. 상업적 목표는 실제 요청에 있을 때 적용하며, 비공개 그림에도 판매 목적을 요구하지 않는다.

이미 명시된 항목은 다시 묻지 않고 확인된 답을 이어받는다. 둘 다 명시돼 있으면 질문 횟수를 채우기 위한 새 질문을 만들지 않는다. 대상만 있다는 이유로 원하는 볼거리까지 안다고 가정하거나, 완성 이미지는 보통 공유한다는 이유로 게시처를 추측하지 않는다. 추가 질문은 결과를 크게 바꿀 공백이 남았을 때만 한다.

빠진 항목을 물었다면 **답을 받은 뒤 방향을 확정하거나 생성·편집을 실행한다.** 기다리는 동안에는 참조·자료 확인처럼 답과 무관한 준비만 진행한다. 침묵을 답으로 간주하거나 에이전트가 자기 질문에 답해 진행하지 않는다. 확인한 두 정보와 그로부터 정한 시각적 선택을 실제 이미지 입력에 반영한다.

같은 작업의 후속 수정에서는 이미 받은 답을 반복해서 묻지 않는다. “알아서”만으로 빠진 두 항목을 임의로 채우지 않는다. 다만 사용자가 명시적으로 “질문 없이 바로 진행”이라고 지시하면 그 최신 지시를 따른다. 단순한 스킬 읽기·설치·요약에는 이 시작 질문을 붙이지 않으며, 이미 허용된 장수·비용·실행 권한을 다시 승인받는 절차로 바꾸지 않는다.

## 2. 만드는 이유와 눈에 보이는 보상을 먼저 결정한다

사용자 정본의 세 축을 **원문 그대로** 사용한다.

1. **내가 보여주고 싶은 것**
2. **이 이미지를 볼 때 제3자가 보고싶어할 것**
3. **상업적으로 보여줘야 할 것**

세 축의 교집합은 채점표가 아니라 장면·초점·재료 선택의 기준이다. 세 번째 축을 단순히 '요구사항 충족'으로 바꾸지 않는다. 감정, 관계, 미적 쾌감, 실루엣·색면·그림체 자체의 매력도 이미지가 주는 보상이다. 모든 요소가 세 축을 같은 비율로 담당할 필요는 없다.

실제 작화 입력에는 이번 그림을 보고 무엇을 **먼저 주목**하고, **어디서 머물고**, **무엇을 발견·느껴야 하는지**를 대상·구도·재료·명암·색으로 연결한다. '자연스럽게, 예쁘게, 귀엽게, 야하게, 잘 팔리게'는 그 자체로 유효한 미적·상업적 목표다. 별도의 서사적 이유를 요구하거나 추상적인 의미로 순화하지 않는다. 사용자가 원하는 매력을 그대로 목표로 삼고, 그 효과를 만드는 표정·몸의 선·포즈·의상·구도·채색을 구체화한다. '역동적으로', '만화처럼' 같은 표현도 요청된 목표로 받아들이고 실제 시각적 수단으로 연결한다. 이 구체화는 사용자의 주문을 정당화하게 하거나 다른 목표로 바꾸기 위한 절차가 아니다. 전문 작법은 **그리기 전에 선택을 개선**하는 지식이며 완성한 프롬프트에 용어를 붙이는 의식이 아니다. 상세 기준: 시각 연출 원칙 (이 파일의 문서 3).

## 2-1. 작법을 조사하고 이해해 실제 선택을 개선한다

보통 일러스트의 작화 방향을 정하기 전에 작법 조사·도메인 지식·체스터턴 (이 파일의 문서 2)을 읽고 적용한다. 일러스트 입문 요령·잘 그리는 법·작가의 직접 해설에서 필요한 기본기를 회수하고, 새 표현·반복 교정·근거의 공백에는 실제 자료를 조사해 읽는다. 확인된 자료가 충분하면 재사용한다. 요구 이해 → 필요한 작법 질문 → 원리와 이유 이해 → 구체적인 작화 선택 → 실제 생성 입력 → 결과 확인으로 잇는다. 전문 용어만 덧붙이거나 완성 후 이론을 붙이는 것으로 대신하지 않는다.

이 방식의 목적은 모델이 일상적인 주문과 분위기를 맞추는 데서 멈추지 않고, 축적된 작법을 실제 제작 판단에 써서 완성도의 하한선을 높이게 하는 것이다. 사용자가 작법이나 별도의 서사적 명분을 설명해야 하는 절차가 아니다. 체스터턴 방식으로 기존 선택이 무엇을 성립시키고 어떤 실패를 막는지 먼저 이해하고, 기본기를 적용한 뒤 그 기능을 다른 수단으로도 유지할 이유가 있을 때 예외를 선택한다. 의미 있는 선택과 WHY·조건·예외는 실제 이미지 입력과 다음 작성자에게 함께 전달한다. 원리의 근거·이번 그림의 해석·실제 입력·결과와 채택은 구별한다.

## 3. 의미의 잠금과 표현 자유를 분리한다

이미지의 의미·인물의 목적·관계·행동 상대·이번 상태·핵심 볼거리·독자가 아는 정보는 충분히 구체화한다. 해당 의미가 바뀌는 결정(필수 구도·정확한 손짓·접촉·시선·정보 공개·의상·문구 등)은 **잠금**으로 적는다. 같은 의미를 자연스럽게 구현하는 세부는 **자유**로 남긴다. 모든 관절·카메라 좌표를 채우지 않는다.

인물은 무엇을 원하고, 누구의 무엇을 보고, 무엇을 감추거나 기대하며 왜 그렇게 반응하는가. 소품은 누구의 물건이고 **이 관찰 방향에서 실제로 보이는 면과 정보가 무엇인가.** 설정에 존재하는 사실을 모두 이번 화면의 글자·장식·등장인물로 만들지 않는다. 화면에 필요한 사람·군중·정보만 쓰되, 핵심 반응·매력·상업적 보상을 비용 절감 때문에 삭제하지 않는다.

## 4. 이미지를 만들어 낼 언어로 스타일을 설계한다

스타일은 키워드를 잔뜩 쌓는 것이 아니다. **선·형태/비례·기본 채색·그림자·팔레트·질감/파편·색점·배경·마감** 중 현재 그림의 매력을 만드는 부분을 결정하고 각각의 역할과 강약을 기술한다. 큰 실루엣과 핵심 표정을 먼저 알아볼 수 있어야 한다. 장식이 많더라도 '어떤 재료처럼 보이는가'와 '이미지의 어디에·왜 존재하는가'를 분리한다.

- **참조의 역할**: `identity / current outfit-state / style / composition / setting / prop / continuity / content proof`를 명시한다. 정체성 참조의 포즈·배경을 복제하지 않고, 화풍 참조가 다른 인물의 얼굴·복장까지 이동시키지 않게 한다.
- **세부 예산**: 시각적 강조는 핵심 대상에 사용하되 풍경·건축·질감 자체가 주역인 경우에는 그곳에 충분히 쓴다. 흰 배경, 얼굴 확대, 보케, 인서트, 종이 같은 컷 경계를 보편법칙으로 만들지 않는다. 배경이 맡는 일(장소 단서/분위기/정보/장관/추상)을 먼저 정한다.
- **실험적 스타일**: 셀채색+기하학적 색면 파편+촘촘한 점·망점은 파편화 셀화 스타일 실험 (이 파일의 문서 7)을 **요청된 경우에만** 선택한다. 2026-10-20 현재 `EXPERIMENT_UNRESOLVED`이며 스킬 전체의 기본 화풍으로 자동 채택하지 않는다.

## 5. 실제 입력은 이유와 맥락을 잃지 않게 구성한다

새 세션·새 이미지 모델은 선행 대화를 자동으로 안다고 가정하지 않는다. 중요한 전후 사건·관계·시각적 WHY·감정·참조 역할·잠금/자유를 **실제 모델에 건네는 본문**에 넣는다. 긴 맥락이 영향을 주는 작업에서는 구조화하되 창작 원문을 길다는 이유로 키워드로 축약하지 않는다. 반대로 역사 로그·실패작의 방어문구·로컬 경로를 프롬프트에 쌓지 않는다.

모델용 본문은 가급적 긍정형의 **무엇이 보이는가**로 작성한다. 과거 실패의 차단 사유는 내부 메모에 두고, 확인된 반복 실패나 필수 금지 대상에만 제한적 부정문을 쓴다. 정확한 글자에 의미가 있을 때만 글자·언어·소유자·표현 채널·읽는 순서·위치를 준다. 텍스트 없는 일러스트에는 의미 없는 표지판·의사 문자를 자동 추가하지 않는다. 출력 목적에 따라 최종 표시 폭/비율을 고려하며, 이미지 내 글자를 작게 밀어 넣지 않는다.

참고: 모델 입력용 구조와 예시 (이 파일의 문서 4). **원문 → 확인 가능한 실제 모델 입력 → 출력 → 사용자 선택**은 서로 다른 증거다. 공홈 이미지 도구의 내부 입력이 보이지 않으면 `actual model-facing input: unverified`라고 쓴다.

## 6. 후보를 보고 판단을 갱신한다

후보 탐색에서는 **단위 시간당 사람이 고를 만한 후보 수**를 중시한다. 현재 요청의 장수·비용·제공 도구 한계 안에서 가능한 병렬·변형 탐색을 활용한다. 별도 실행 스크립트나 제공되지 않은 병렬 기능이 있다고 가정하지 않는다. 후보 풀과 동시 제출량은 별개이며, 특정 장수를 기본값이나 추가 생성 승인으로 간주하지 않는다. 개별 실패율만으로 병렬 수를 낮추지 않고 실제 완료 후보/시간이 줄어드는 과부하가 확인되면 병목과 제출량을 조절한다. 도구가 한 번에 한 장만 지원하면 그렇다고 알린다.

후보는 파일 생성 성공만으로 평가하지 않는다. **의도·인물 정합성 / 구도·행동·시선 / 선·색·질감 위계 / 실제 시각적 보상**을 구분해 본다. 시각 평가를 요청받은 범위에서 실제 이미지를 보고 구체적으로 말한다. 사용자 채택은 `USER_SELECTED_SUCCESS`(사용자 선택 사실), 아직 검증되지 않은 것은 `EXPERIMENT_UNRESOLVED`, 미채택 비교 후보는 `BENCHMARK_CANDIDATE`, 실패 교정 사례는 `FAILURE_EXAMPLE`로 기록한다. 선택된 한 장이 모든 문구의 구현 성공이나 내부 전송 경로의 완전성을 입증하지는 않는다.

새 구도·핵심 액션을 탐색할 때는 **새 생성+연속성 참조**, 이미 마음에 든 이미지의 일부를 고칠 때는 **선택 원본에 대한 편집**을 구분한다. 선택 원본을 보존하고 수정본을 별도로 취급한다. 불량 결과를 무분별하게 다음 참조로 재사용하지 않는다. 모자란 점이 확인되면 관련 층위(의도/참조/구성/표현/전달/도구)를 진단하고, 성공했던 부분은 보존한 채 가장 작은 유효 수정을 한다.

## 7. 매체 경계·상태 경계

- **웹툰의 제작 조건은 조건부**: 컷 수·분리 띠·흰 원고·세로 편집·폰에서 보는 식자·고정 캔버스·밀도 비율은 해당 프로젝트가 요구할 때만 적용한다. 단일 그림에는 주목 관계와 정보 배분의 WHY를 옮긴다.
- **실행은 도구의 실제 기능으로**: 이 스킬은 생성 API·인증·로컬 서버·실행 스크립트를 제공하지 않는다. 프롬프트와 실제 참조 파일을 현재 도구가 지원하는 방식으로 전달하고, 도구별 지침을 따른다. 읽은 것과 실행한 것을 구별한다.
- **실험은 조건부**: 특정 배치·문구 압축·고정 좌표·새 화풍의 효과는 해당 조건에서 확인한다. 기술 PASS나 한 번의 선택을 일반 법칙으로 바꾸지 않는다. 파편 셀채색 실험은 요청된 경우만 적용한다.
- **상태와 출처**: 근거·가설·적용 범위 (이 파일의 문서 6). 공개 패키지에 없는 과거 이미지·원고·세션을 실제 첨부한 것처럼 취급하지 않는다.

## 읽기 경로

- **보통 단일 일러스트**: 이 `SKILL.md`, 작법 조사·체스터턴 (이 파일의 문서 2)과 시각 연출 (이 파일의 문서 3), 필요하면 모델 입력 패턴 (이 파일의 문서 4).
- **새 그림체/파편·점묘 실험**: 추가로 선택형 스타일 실험 (이 파일의 문서 7). 이때도 요청하지 않은 생성은 하지 않는다.
- **장문·참조 충돌·규칙의 WHY 확인**: 상세 원칙과 이유 (이 파일의 문서 5) 및 근거·적용 범위 (이 파일의 문서 6). 상세 원칙의 예시·양식은 필요한 경우에 쓰며 현재 사용자 지시와 이 입구의 최신 결정이 우선한다.
- **다컷 웹툰**: 해당 웹툰 프로젝트의 별도 스킬과 현재 제작 계약이 주관한다. 이 스킬은 충돌하지 않는 공통 작화 판단을 보탠다.


---

# 문서 2: 일러스트 작법 조사·도메인 지식 적용·체스터턴의 울타리

# 일러스트 작법 조사·도메인 지식 적용·체스터턴의 울타리

2026-10-21 공개판. v2.1에서 채택한 작법 적용 지침을 이어받는다. 보통 일러스트의 작화 방향을 정하기 전에 읽는다. 이 문서의 적용 방식은 사용자 채택이며, 여기 든 예시 조합의 이미지 생성 성과까지 검증됐다는 뜻은 아니다.

## 왜 조사하고 도메인 개념으로 풀어 쓰는가

사용자는 예쁘고 귀엽고 야하고 잘 팔리는 그림, 자연스럽거나 힘 있는 포즈처럼 원하는 효과를 일상어로 말할 수 있다. 그 주문만으로 충분히 유효하며, 사용자가 전문 용어나 서사적 명분을 갖춰야 하는 것은 아니다. 이를 구현하는 작법을 찾고 표현을 결정하는 책임은 제작 담당자에게 있다.

기존 제작 과정에서 확인한 문제는 '이런 그림을 만들어라'라는 목표와 분위기만 맞추고, 알고 있거나 찾아볼 수 있는 전문 작법을 실제 설계에 충분히 쓰지 않았다는 것이다. 그래서 완성 뒤 그럴듯한 작법 해설을 붙이는 대신, 그리기 전에 축적된 지식으로 첫 선택부터 개선해 완성도의 하한선을 높이려 한다. '사전지식 활성화'는 이 행동상의 간극을 설명하는 말이다. 모델 내부 작동이나 품질 향상률을 측정했다는 주장은 아니다.

입문 요령과 '일러스트 잘 그리는 법'도 필요한 출발점이다. 검색어와 설명을 점차 실루엣, 제스처, 동세선, 구조와 비례, 원근, 명도 덩어리, 초점, 색상·채도·색온도 대비, 에지, 소재 표현처럼 이번 문제에 맞는 도메인 개념으로 좁힌다. 용어를 나열해 전문적으로 보이게 하는 것이 목적이 아니다. 그 개념을 이해했기 때문에 어느 선택을 왜 바꿨는지가 실제 그림 지시에서 드러나야 한다.

## 필요한 자료를 읽고 실제 결정을 만든다

먼저 현재 목적·독자·화풍·참조와 이미 채택한 매뉴얼에서 필요한 지식을 회수한다. 확인된 자료가 이번 문제에 충분하면 재사용한다. 새 표현, 반복 교정, 해석의 불확실성, 근거가 없는 처방, 사용자의 조사 요청이 있으면 입문서·작화 매뉴얼·작가나 교육자의 직접 해설을 찾아 실제 본문과 예시 설명을 읽는다. 검색 결과의 제목·요약만 보고 적용했다고 하지 않는다. 모든 이미지마다 같은 검색을 반복하거나 자료 수를 채우는 절차는 아니다.

출처는 저자·제목·URL 또는 책의 판본과 해당 절을 확인할 수 있게 둔다. 작가 본인의 강의와 제작 해설, 출판사·교육기관·도구 제공사의 교재를 우선하고, 같은 사이트의 사용자 기고는 그 저자의 실무 해설로 구분한다. 서로 다른 처방은 어느 매체·목적·조건에서 하는 말인지 먼저 읽는다. 접근하지 못한 자료를 읽었다고 쓰거나, 근거를 확인할 수 없는 조항을 만들어내지 않는다. 조사 도구가 없으면 현재 확인 가능한 자료의 범위에서 판단하고 그 한계를 필요한 지점에만 밝힌다.

작업은 **요구 이해 → 필요한 작법 질문 → 자료와 원리 이해 → 구체적 작화 선택 → 실제 생성 입력 → 결과 확인**으로 잇는다. 예컨대 '자연스럽게'라는 목표를 받아 몸의 흐름이 문제인지, 지지·접촉이나 원근이 문제인지 구별하고, 그 부분의 원리를 읽어 자세·힘의 방향·관찰 위치를 결정한다. '자연스럽게 그려라' 뒤에 전문 용어만 덧붙이는 것으로 끝내지 않는다. 충분히 합의된 취향과 평범한 표현 선택을 매번 사용자에게 다시 설명하게 하지 않는다.

## 체스터턴: 기본기의 기능을 이해한 뒤 유지하거나 예외를 택한다

주요 작화 선택을 정하거나 바꾸기 전에 **기존 처방이 무엇을 성립시키고 어떤 실패를 막는지** 먼저 이해한다. 이유는 현재 매뉴얼의 설명, 실제 입력·결과, 사용자 채택에서 회수한다. 원래의 기능을 모른 채 오래됐거나 문장이 길다는 이유로 지우지 않는다. 먼저 축적된 기본기를 충실하게 적용하고, 다른 수단으로도 그 기능을 살릴 이유가 있을 때 의도적인 예외를 선택한다.

예를 들어 '주제를 돋보이게 한다'는 목적을 이해했다면 배경을 언제나 비우는 숫자 규칙으로 고정하지 않는다. 명도·채도·색온도·에지·묘사량·배치 중 현재 화풍에 맞는 수단으로 주제의 위계를 만들 수 있다. 배경 자체가 볼거리인 그림에서도 주목 관계를 설계할 수 있다. 마찬가지로 동세를 살리기 위한 과장은 해부학을 모르는 실수와 다르고, 단순화한 구조는 포즈·정체성·의도한 매력이 읽히는지를 기준으로 판단한다.

규칙의 이유가 여전히 불분명하면 원문·근거를 더 읽고, 필요한 경우에만 어떤 항목과 맥락이 비어 있는지 구체적으로 묻는다. 그동안 해당 규칙을 유지하고 무관한 일을 진행한다. 이미 설명받은 이유를 다시 묻거나, 모든 작은 선택에 별도 승인표를 붙이지 않는다. 최신 사용자 결정이 기존 처방을 바꿨다면 그 이유와 적용 범위를 함께 이어받는다.

주요 변경은 필요할 때 **기존 실제 표현 → 제안 표현 → 보존·변경한 기능과 이유 → 매뉴얼의 해당 설명 → 이번 그림에 적용한 해석 → 실제 결과의 확인 범위**로 설명한다. 이는 중요한 판단을 검토 가능하게 하는 방식이다. 매 문장·매 이미지에 이 형식의 보고서를 의무적으로 만드는 절차는 아니다.

## 현재 읽은 작법과 적용 예

아래는 2026-10-20 직접 읽은 출처와 그 원리를 현재 작업에 옮기는 예다. 예시의 프롬프트 선택은 제작 담당자의 적용 판단이며 원저자가 이미지 생성 도구에 대해 한 주장이 아니다.

| 출처와 읽은 부분 | 회수한 작법과 기능 | 이번 그림에서 결정할 것의 예 |
| --- | --- | --- |
| [Stan Prokopenko, How to Draw Gesture](https://static.proko.com/static/course-lesson/how-to-draw-gesture) — Lesson Notes의 gesture, line of action, relaxed/tense curves | 세부 윤곽보다 몸 전체를 잇는 흐름과 동작·감정을 먼저 잡는다. | '자연스럽고 여유 있게'라면 몸통과 다리의 이어지는 흐름, 긴장이 남는 부분과 풀린 부분을 정해 몸짓을 지시한다. 동세선을 완성 그림에 선으로 인쇄하라는 뜻은 아니다. |
| [Konart, Understanding Grayscale/Monochrome Art](https://tips.clip-studio.com/en-us/articles/2893) — VALUES, VALUES IN COMPOSITION | 명도 차이와 덩어리가 초점을 조직한다. 대비의 배분과 주변 관계를 읽는다. | 검은 의상과 어두운 배경이 겹쳐 읽히지 않으면 필요한 실루엣 주변의 명도 관계를 조정한다. 모든 곳의 대비를 무조건 높이지 않는다. |
| [SteffyStyle, Highlight characters in your drawing with 3 basic tips](https://tips.clip-studio.com/en-us/articles/7181) — focal point, luminosity/temperature/saturation/detail contrast | 인물과 배경의 관계는 밝기뿐 아니라 색온도·채도·묘사량의 차이로도 만들 수 있다. | 인물이 주역이면서 복잡한 배경도 필요한 경우, 배경을 삭제하기 전에 두 층의 대비·묘사량을 조정한다. 특정 보색·흐림 효과를 항상 강제하지 않는다. |

관객과 캐릭터의 매력은 이 기법을 선택할 목적이다. 남캐·여캐라는 이름만으로 어필 공식을 고정하지 않는다. 같은 남캐라도 인물의 미형·귀여움·몸·태도·카리스마·성적 매력 중 이번 독자와 의뢰가 원하는 것을 읽고 그에 맞는 비례·실루엣·표정·동작·의상·빛을 선택한다. 그 취향을 매번 사용자가 전문적으로 풀이해야 하는 것은 아니다.

## 그림 모델과 다음 작성자에게 무엇을 전달하는가

제작자는 매뉴얼의 개념과 적용 조건을 이해하고 판단한다. 이미지 모델에는 **선택한 시각적 수단, 작동할 위치·강약·관계, 왜 이번 매력에 필요한지, 보존할 것과 표현 자유**를 실제 입력 본문으로 전달한다. 유용한 도메인 용어도 그 의미가 드러나는 작화 설명과 함께 쓴다. 파일 경로·문헌명·'매뉴얼 준수'라는 한 줄이 의미를 대신 전달하지 않는다. 반대로 매뉴얼 전문이나 조사 이력 전체를 매번 프롬프트에 붙이지 않는다.

예: '남캐를 매력적으로, 제스처 강조'에서 끝내지 않고, 의뢰가 원하는 여유로운 태도에 맞춰 몸통과 다리의 흐름, 긴장과 이완의 차이, 시선과 의상 실루엣이 어떻게 읽힐지 설명한다. 이 구체화는 예시이며 모든 남캐에 같은 포즈를 넣는 기본값이 아니다.

새 세션이나 다른 작성자에게 넘길 때도 요구·선택·WHY·적용 조건·예외·근거를 함께 건넨다. 다음 사람이 이전 대화를 자동으로 아는 것처럼 파일 몇 개나 요약 키워드만 넘기지 않는다. 원리의 근거, 이번 그림에 대한 해석, 실제 모델 입력, 생성된 그림, 사용자의 채택은 서로 다른 증거다. 문서에 적었다는 것과 실제로 적용했다는 것, 작법 근거와 이미지 생성 성공률을 구별한다.

이 방식은 반복 제작 중 선택의 기능과 실패 이유를 회수해 온 경험에서 정리했다. 공개판에는 개인 프로젝트의 원고·대화·실행 기록을 넣지 않고, 적용에 필요한 이유와 조건을 본문으로 전달한다. 만화 전용 컷·식자 조건을 단일 일러스트에 자동 이식하지 않는다.


---

# 문서 3: 제작 경험을 범용 이미지 연출로 재구성한 원칙

# 제작 경험을 범용 이미지 연출로 재구성한 원칙

**상태: v2.2 공개판 · 2026-10-21.** 제작 경험에서 가져온 기능과 이미지 모델에 대한 적용 가설을 구별한다. 이 문서가 모든 처방의 효과를 실증했다는 뜻은 아니다.

## 무엇을 갱신하는가

기존 만화 제작 과정에서 이미지 생성의 좋은 결과를 반복 가능하게 하려다 발견한 것은 '특정 프로젝트의 프롬프트를 모든 이미지에 넣는다'가 아니다. 핵심은 **그림을 주문하기 전에 미적·서사적 결정을 제대로 내린다**는 것이다. 세 축(내가 보고 싶은 것 / 제3자가 보고 싶은 것 / 상업적으로 보여줘야 할 것)을 구상에서 실제 시각 언어로 전환하고, 이미지 모델은 이 결정의 구현 파트너로 취급한다.

이전 접근에서 잘못하기 쉬운 양극단:

- 의도를 비워 놓고 '알아서 최고 퀄리티'만 요청한다 → 모델이 무엇을 강조해야 하는지 모른 채 익숙한 장식으로 채운다.
- 모든 손·발·관절·좌표·장식을 고정한다 → 이미지의 자연스러움·균형·상상할 여지를 빼앗고 규칙 사이 충돌을 만든다.

**판단 원리:** 그 선택을 바꾸면 장면의 뜻·주목 순서·표현할 관계·매력이 바뀌는 것은 감독이 정한다. 그 의미를 유지하는 여러 해법이 가능하면 모델이 고르게 한다. 이런 분담은 프롬프트가 짧아야 한다는 규칙도, '세세히 쓰면 실패한다'는 실증도 아니다.

## 선택 전에 작법과 기능을 회수한다

작법 조사·체스터턴 (이 파일의 문서 2)을 읽고 요구를 실루엣·제스처·구조·비례·명도와 색의 위계 등 필요한 개념으로 해석한다. 자료의 설명과 이번 그림에 대한 적용 판단을 구별하고, 그 원리가 실제로 바꾸는 구도·몸짓·강약·빛을 먼저 정한다. 기본기의 목적을 이해하기 전에는 형식적인 숫자나 이유 없는 금지문으로 바꾸지 않는다. 다른 해법을 택할 때도 원래 살리려던 기능과 사용자 매력 목표를 보존한다.

## 하나의 이미지에 적용하는 연출 순서

### 1. 관람 경험과 볼거리를 정한다

보는 사람에게 처음 다가올 덩어리/선/얼굴/빛/물체가 무엇인가? 거기서 더 보게 되는 표현은 무엇인가? 긴장·위로·불길함·속도·우아함·비정상적 아름다움처럼 감정어만 적지 않고 그 경험의 시각적 실체를 고른다. '자연스럽게, 예쁘게, 귀엽게, 야하게, 잘 팔리게'라는 직접적인 요구도 그 자체로 그림의 목적이 된다. 별도의 서사적 정당화를 요구하지 않고, 아름다움·귀여움·성적 매력·판매력을 추상적인 의미나 무난한 미감으로 순화하지 않는다. 사용자가 보고 싶은 요소와 상업적으로 보여줘야 할 매력을 보존하고, 그 매력이 실제로 드러나게 할 표정·몸의 선·포즈·의상·구도·채색을 선택한다. 여백으로만 정갈한 그림을 만드는 것을 목표로 삼지 않는다.

### 2. 의미·정보·물리적 관계를 결정한다

누가 누구를 보며 무엇을 하거나 숨기고 있는가? 누구에게서 무엇을 발견해야 하는가? 인물이 있는 단일 일러스트도 이 관계의 연기로 살아날 수 있다. 인물 포즈 자체가 스타일·매력의 보상이면 그 자세를 정하고, 그렇지 않으면 몸과 카메라의 구현 자유를 둔다. 사용자가 지정한 특정 몸짓·각도·크롭이 중심이면 고정한다.

이야기의 전체 설정과 실제 화면에 보이는 정보는 다르다. 예컨대 뒷면이 보이는 서류의 내용은 문맥으로 전달하되 화면에서 그 내용을 그리라는 지시로 변환하지 않는다. 모든 관계자를 등장시키거나 화면 밖 설명을 자막으로 채울 필요가 없다.

### 3. 시각적 위계를 설계한다

실루엣, 주요 명암 덩어리, 시선과 제스처, 색대비, 선의 강약, 질감·파편/점, 배경 상세의 순위를 고른다. 이것은 자원을 실제로 계량한 주장이 아니라 **눈의 주의 요구를 배분한다는 디자인 판단**이다. 평면 그래픽 요소가 많으면 그림 전체가 복잡해질 수 있다. 복잡함을 어디에 쓸지와 어느 부분의 조용함이 그 효과를 돋보이게 할지 같이 정한다.

배경 역할을 다음 중 하나 또는 둘 정도로 정한다: 주제의 분리 / 장소의 증거 / 이야기 정보 / 분위기 / 규모·세계관 / 독립적 볼거리. 빈 공간을 무조건 채우거나, 서사적 그림이라는 이유로 모든 카메라를 인물의 POV에 묶지 않는다. 핀업, 홍보 포스터, 초상, 추상·풍경은 각각 합당한 화면 문법을 가진다.

### 4. 작법 개념으로 판단하고 구체적인 표현과 WHY를 전달한다

원자료의 `composition`, `acting`, `detail`, `finish`처럼 기능별로 생각하되 모든 모듈을 매 이미지에 붙이지 않는다. 예시:

- '일본 만화풍에 집중선' → 이번 이미지에서 충격의 방향을 읽게 해야 할 때만 선을 선택.
- '빛나는 보라색' → 인물의 어두운 감정이 차가운 베이스색과 따뜻한 파편 하이라이트의 대비로 읽혀야 한다.
- '배경을 단순하게' → 캐릭터의 세부 채색이 이번 이미지의 주역이어서 배경의 세부 명암을 덜고 인물 채색에 시선이 머물게 한다.

업계 작법이 보편적인 시각 효과를 설명할 수는 있어도, 그 용어가 현재 모델에서 특정 메커니즘을 자동으로 호출했다는 증거는 아니다.

### 5. 참조를 역할별로 고른다

정체성·현재 복장·화풍·화면 배치·공간·소품·연속성을 분리한다. 가장 적은 수의 유효 참조부터 시작한다. 첨부가 두 장이면 번호와 역할을 본문에서 일치시킨다. 스타일 참조의 인물·포즈를 새 주인공으로 가져오지 않는다. 정체성 참조의 화면을 그대로 복사하라는 뜻도 아니다.

새 캐릭터 디자인을 **스타일 먼저 맞추기**로 탐색할 때는: 기존 작품의 style-only 참조로 후보 씨드 → 사람이 디자인 선택 → 선택 씨드를 identity로 삼아 필요한 시트 제작. 이는 캐릭터 반복 제작의 상황별 전략이다. 기존 인물의 특정 이미지를 편집하는 의뢰에는 이 경로를 강제하지 않는다. 실제 style 이미지가 제공되지 않았다면 파일명만으로 화풍의 시각적 보존을 보장할 수 없다.

### 6. 실제 입력을 조립한다

원래의 WHY, 인물에게 일어난 일, 보존해야 할 정체성·상태, 관객이 알아야 할 사실과 숨겨 둘 정보, 화풍의 작동 위치를 실제 모델용 본문으로 제공한다. 공급자에게 전달되지 않는 서류 경로나 모듈명만 적지 않는다. 복잡한 일러스트에서 긴 맥락 자체를 불필요한 것으로 간주하지 않는다. 중복 운영 기록·과거 실패 방어문은 제외한다.

### 7. 사람에게 시각적 후보를 보여주고 교정한다

요청 범위/도구 한계 내에서 여러 구성이나 표현 비율의 후보를 만든다. 선택을 기다리는 동안 이전 선택 원본은 그대로 둔다. 부족한 부분은 **정보 전달·의도·참조 혼입·실제 도구 입력·이미지 구현·사용자의 미적 취향** 중 어디에서 시작됐는지 진단한다. 프롬프트가 길어졌다는 것과 개선은 관계가 없다. 결과 미감을 실제로 보고 교정한다.

## 매체별 기능을 분리해 가져온 작화 판단

| 원본 모듈 | 범용 작화에서 판단할 내용 | 작품 전용으로 남는 것 |
|---|---|---|
| `intent` | 보여줄 가치·WHY·관계·독자와 상업적 보상 | 결말 전체를 요구하는 연재 입력 |
| `reference` | identity/outfit/style/composition 등 참조 역할 | 특정 캐릭터 등록·참조 해시 계약 |
| `continuity` | 같은 인물·물체·색과 상태의 불변·변화 | 회차별 정본 장부와 재생성 의무 |
| `composition` | 시각적 위계·숏·크롭·주목 순서 | 만화 패널의 위→아래 배분 |
| `acting` | 상대·의도·행동에 반응하는 몸·표정 | 컷 사이 발화 타이밍 |
| `detail` | 보이는 정보의 선택·복잡성 예산·배경 역할 | 특정 밀도 수치 및 안쪽 무대 |
| `finish` | 채택 화풍의 형태·선·색·질감 일관성 | 만화 식자·선화 자동 규격 |
| `lettering` | 글자가 있을 때 정확한 원문·소유·대비 | 만화 화자 꼬리·댓글 UI의 프로젝트 문법 |
| `sequence/rhythm/boundary` | 정적·시선 흐름·구도 내부 리듬이라는 간접 교훈 | 컷 수·분리 띠·거터·무테·경계 넘기 |

이 표는 제작 기능의 의미상 대응이다. 문서의 기능을 보존했다는 확인과 각 문구가 현재 이미지 모델에서 독립적으로 효과를 냈다는 실증은 다르다. 문구 압축이나 기능 분류 자체를 새 시각적 품질의 검증으로 취급하지 않는다.

## 도구와 매체를 분리한 결론

한국어 세로툰 제작에서 **컷 시트 후보 → 사용자 선택 → 세로 편집**을 쓰는 경우가 있다. 그러나 그 구조를 단일 일러스트 작업으로 끌어와 원하지 않은 여러 컷/인물 복제를 만드는 것은 목표와 정반대다. 단일 일러스트는 한 화면의 시각적 우선순위와 스타일 설계, 첫 후보, 비교 및 선택 후 수정이라는 **의사결정 구조**만 가져온다.

고정된 흰 페이지·중앙 무대·컷 밀도 비율에는 만화의 쉼과 국소 경계 넘기 이유가 있었으므로 무턱대고 제거하지도, 단일 이미지에 강제하지도 않는다. 특정 실행 경로에서 전송이 성공했다는 사실을 다른 이미지 도구의 검증으로 주장하지 않는다.


---

# 문서 4: 이미지 모델 입력·참조·후보 판정 패턴

# 이미지 모델 입력·참조·후보 판정 패턴

이 문서는 실제 그림에 필요한 내용을 조립하기 위한 **가변적인 구조**다. 빈칸을 모두 채우는 서류가 아니며, 사용자와 공유하지 않은 별도의 승인 단계를 만들지 않는다.

## 입력 전에 정할 것

작법 조사·체스터턴 (이 파일의 문서 2)으로 필요한 원리와 기능을 이해한 다음 아래 입력을 작성한다. 조사 출처·매뉴얼의 설명과 이번 그림의 적용 해석은 필요한 작업 메모에 두고, 모델 본문에는 선택한 도메인 개념과 그 개념을 구현할 가시적 관계·위치·강약·WHY를 전달한다. 문헌 이름이나 키워드만 쓰거나 매뉴얼 전문을 매번 붙이는 것으로 대신하지 않는다.

## 1. 모델용 입력의 구조

```text
IMAGE INTENT / WHY
- 내가 보여주고 싶은 것:
- 제3자가 이 그림에서 보고 싶어할 것:
- 상업적으로 보여줘야 할 매력:
- 이번 이미지를 볼 때 먼저 읽힐 것 → 머물 것 → 느낄 것:

WHAT IS HAPPENING / CONTEXT
- 장면·인물 상태·사건/감정의 이유:
- 누가 누구에게 무엇을 하며, 무엇이 보여야 하나:
- 화면에 그리지는 않지만 해석에 필요한 문맥:

VISIBLE CONTENT / REFERENCE ROLES
- 실제 보이는 인물·물체·상태(필요한 것만):
- 참조 1: identity / outfit / style / composition / setting ... 중 정확한 역할
- 참조 2: ...
- 보일 면·글자·행동·접촉·색·소유 관계:

VISUAL DIRECTION
- 선택한 작법 개념과 이번 그림에서 살릴 기능:
- 그 기능을 구현할 구체적인 관계·위치·강약과 WHY:
- 실루엣/표정/시선의 중심:
- 구도·관찰 관계·초점의 이유:
- 기본 그림체(선·색·그림자·형태):
- 특징적인 시각 언어(이번에 쓰는 곳/조용한 곳):
- 배경 역할·색/디테일의 우선순위:

MUST KEEP / CREATIVE FREEDOM
- 의미를 바꾸므로 유지할 선택:
- 의미를 유지하며 모델이 결정할 표현:

TEXT IF ANY
- 정확한 문자열 / 소유자·채널 / 읽는 순서·상대 위치:

OUTPUT
- 이미지 용도·형식·비율·텍스트 가독성·필수 조건:
```

원문 WHY/행동/관계가 복잡하면 충분히 길게 쓴다. 간단한 일러스트는 필요한 줄만 사용한다. `must keep`이 작은 구도를 강제하는 것과 `creative freedom`으로 핵심을 비우는 것은 둘 다 실패 원인이다.

## 2. 스타일-only 실험을 위한 구체적 역할 지도

```text
REFERENCE ROLES
1. [실제로 첨부한 인물 정본] — identity / current outfit ONLY.
   이 참조의 포즈·카메라·배경은 새 이미지의 구도 계약이 아니다.
2. [실제로 첨부한 별도의 스타일 예시] — style ONLY.
   그림 속 인물의 얼굴·의상·포즈는 옮기지 않는다.
3. [실제로 첨부한 구성 예시, 필요할 때만] — composition ONLY.
```

첨부가 없는 역할 줄은 빼고, 그 부재를 정확히 표시한다. 이미지 2장이 서로 충돌하면 어떤 특징을 어느 참조에서 가져올지 결정한다. 새로운 2D 스타일 실험 때 이전 실패 그림을 단독 style 기준으로 삼으면 실패한 표현이 고착될 수 있다. 무엇이 좋았는지 명시하고 해당 부분만 비교 자료로 사용한다.

## 3. 수정인지 변형인지

- **편집**: 사용자가 선택·제공한 원본을 기초로 지정 영역(예: 머리카락 그림자에 파편 더하기)만 고친다. 나머지 얼굴·표정·포즈·의상·구도는 가능한 한 보존한다. 도구가 이러한 국소 보존을 보장하지 못하면 그 한계를 말한다.
- **동일 설정의 새 구도**: 이전 선택본을 continuity/identity 근거로 쓰되 새로운 조명·포즈·프레이밍을 만드는 별도 생성이다. 이전 완성 이미지를 직접 덧칠하는 편집으로 취급하지 않는다.
- **새 스타일 씨드**: 특정 인물 채택 전의 화풍 탐색이라면 어떤 정체성을 잠그는지부터 정한다. style-only는 다른 인물의 정체성을 복제하는 지시가 아니다.

## 4. 출력 확인의 구분

| 종류 | 확인할 수 있는 것 | 그것만으로 확인되지 않는 것 |
|---|---|---|
| 원문·첨부 | 원문 바이트, 참조 파일, 의도한 입력 구성 | 도구 내부 모델에 모든 의미가 그대로 전달되었는가 |
| 가시적 실제 입력 | 사용자에게 드러난 prompt/수정사항 | 내부 전처리·revisedPrompt가 동일한가 |
| 도구 완료 | 요청이 수락되어 결과 파일이 생성됨 | 인물의 감정·작화 스타일·글자 품질이 맞는가 |
| 시각 검토 | 실제 보이는 표정·형태·색·질감·구도의 부합 | 단독 문구가 결과를 인과적으로 만들었는가 |
| 사용자 선택 | 그 후보를 사용하기로 골랐음 | 모든 세부 지시가 충족되었거나 재현성이 검증되었는가 |

사용자가 미술적 평가는 직접 하겠다고 하면 후보 전달과 객관 자료를 우선하고 보지 않은 이미지를 점수화하지 않는다. 검토 요청이 있으면 구체적으로 무엇이 보이고 무엇이 부족한지 분리한다.

## 5. 원인별 최소 수정

| 관찰된 문제 | 먼저 볼 층 | 바꿀 범위의 예 |
|---|---|---|
| 인물이 다른 사람 같음 | identity 참조·실제 참조 결합·현재 의상 | 참조 역할과 실제 이미지 먼저 교정, 질감 키워드는 그대로 |
| 표정은 예쁜데 이야기가 안 읽힘 | WHY·인물의 목적/상대·구도 | 행동 상대·반응 관계·가시 행동을 분명히, 관절 지정은 필요할 때만 |
| 배경만 화려하고 인물은 평범 | 세부 예산·스타일 표현 위치 | 파편/점묘를 인물 채색 경계로 보내고 배경의 경쟁 명암 줄이기 |
| 파편 대신 글리터·보케 | 질감 형태·스케일·배치 | 큰 색면→중형 다각형→미세 색점의 전이를 서술하고 국소 비교 |
| 손·소품 의미가 바뀜 | 핵심 물리 관계·참조·모델 구현 | 필수 접촉/사용 면을 잠그고 같은 오류가 계속되면 국소 수정 또는 다른 후보 선택 |
| 불필요한 텍스트/소품 추가 | 실제로 보일 정보·긍정형 목록 | 현재 화면에 필요한 대상과 정확한 텍스트만 명시, 악화가 반복되면 조건부 방어 |

부분 보완의 실효성은 새 이미지에서 확인한다. 무리하게 고정 조건을 누적해 다른 좋은 부분까지 망가뜨리지 않는다.


---

# 문서 5: 상세 원칙의 위치

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


---

# 문서 6: 근거·가설·적용 범위

# 근거·가설·적용 범위

## 이 스킬의 지위

IGP는 “가설단계에서 이미지 모델에 생성협조를 요구한” 데서 출발한 제작 지침이다. 제작 경험과 미술 작법을 토대로 선택을 설명하고 이미지 모델에 구현을 요청한다. 사용자의 좋은 실사용 결과 피드백은 유지하되, 모델 내부 기제를 증명하거나 개별 문구의 품질 향상률·보편적 재현성을 검증했다고 확대하지 않는다.

**현재 확인 범위(2026-10-21): 긍정적인 실사용 피드백은 오로지 Codex에서 ima2로 이미지를 생성한 경로에서만 확인했다.** ima2는 여기서 실행 도구를 가리키며 정확한 내부 백엔드 모델 버전·전처리까지 검증했다는 뜻은 아니다. 공홈 Library에 파일을 추가하고 실제로 읽게 해 지침으로 적용할 수 있으며, Codex에서는 IGP와 ima2를 함께 사용할 수 있다. 이 사용 가능성과 모델별 효과 검증은 다르다. 다른 제공자에 대한 효과나 무작위 대조 실험으로 입증된 인과 효과는 주장하지 않는다.

| 층위 | 확인하거나 판단하는 것 | 그 사실만으로 확정하지 않는 것 |
| --- | --- | --- |
| 작법 자료 | 저자가 설명한 원리·목적·조건 | 특정 생성 모델에서 같은 효과가 자동 발생함 |
| 제작자의 가설 | 이번 요구에 어떤 시각 수단이 맞는지와 WHY | 유일한 정답·확정된 작동 기제 |
| 실제 전달 | 도구에 넣은 본문·첨부·옵션 중 관찰 가능한 것 | 숨은 재작성·전처리 뒤의 입력 동일성 |
| 생성 결과 | 실제 보이는 형태·표정·빛·질감·정보 | 한 문구가 그 결과를 인과적으로 만들었음 |
| 사용자 선택 | 사용자가 그 후보를 좋게 보고 선택함 | 모든 지시 구현·재현성·일반 이론의 확정 |

이 구분은 작업 판단에 쓰며 모든 이미지에 검증 보고서를 붙이라는 절차가 아니다. 내부 입력이 보이지 않을 때만 그 확인 한계를 필요한 지점에 적는다.

## 공개판에 남긴 기능과 WHY

- **세 축과 직접적인 매력:** 창작자·관객·상업적 볼거리를 함께 판단한다. 예쁘게·귀엽게·야하게·잘 팔리게라는 주문을 서사적 정당화 요구로 바꾸지 않는다. 성별 이름만으로 매력 공식을 고정하지 않는다.
- **문맥을 보존하는 전달:** 행동·관계·감정·정보차·전후 이유가 바뀌면 그림 해석도 바뀔 수 있다. 장문이라는 이유로 버리지 않고 구조화한다. 불필요한 운영 이력은 실제 이미지 입력에서 덜어낸다.
- **체스터턴과 작법:** 기존 규칙이 어떤 기능을 지키고 어떤 실패를 막는지 이해한 뒤 적용하거나 예외를 고른다. 미술 지식은 제작 전에 선택을 바꾸는 데 쓰고, 완성 뒤 용어를 붙이는 데서 끝내지 않는다.
- **의미 잠금과 구현 자유:** 의미·정체성·핵심 관계를 고정하고 같은 뜻을 살리는 구체적 표현은 모델이 풀 수 있게 한다. 중요한 정확한 손짓이나 카메라가 요청의 핵심이면 그것도 잠근다.
- **참조·복잡성·배경의 역할:** 정체성과 구도·스타일을 구별하고, 어디에 시선과 표현을 쓸지 판단한다. 흰 배경·얼굴 확대·낮은 밀도를 보편법칙으로 만들지 않는다.
- **원본과 선택 보존:** 새 구도와 원본 편집을 구별한다. 사용자 선택을 존중하고 관련 부분을 개선하며 성공을 주장할 범위를 실제 관찰에 맞춘다.

## 실험과 매체 경계

파편 셀채색 문서는 요청된 경우만 쓰는 미해결 스타일 연구다. 실험 비교 조건은 후보 장수나 비용을 자동 승인하지 않는다. 작품별 컷 수·원고 크기·식자·흰 띠·고정 밀도·합본 방식은 그 작품의 계약이 소유한다. 이런 선택의 기능을 이해하는 것과 단일 그림에 수치를 이식하는 것은 다르다.

## 공개판의 계보

v1.2의 공통 이미지 원칙 → v2.1의 직접적인 미적 목표·작법 조사·체스터턴 보강 → v2.2의 독립 공개 스킬·기본 단독 이미지 적용으로 이어졌다. 개인 프로젝트에서 나온 제작 경험을 범용 작화 판단으로 정리했으며, 원고·개인 세션·과거 원본 이미지·인증·설치 영수증·로컬 실행 하네스는 배포하지 않는다. 문서의 출처·조건·교훈은 본문과 참고자료에서 확인할 수 있고, 비공개 저장소 접근 없이 적용할 수 있다.

작법 출처와 해석 구분은 작법 조사·체스터턴 (이 파일의 문서 2), 문맥 보존과 상세 이유는 상세 원칙 (이 파일의 문서 5)에 있다. 이 패키지는 이미지 생성 도구나 도구 사용 허가 자체를 제공하지 않는다.


---

# 문서 7: 선택형 그림체 실험 — 파편화 셀채색 · 색점·망점

# 선택형 그림체 실험 — 파편화 셀채색 · 색점·망점

**상태: `EXPERIMENT_UNRESOLVED`.** 셀화 색면이 작은 조각과 미세 색점으로 분해되는 표현을 탐색하는 선택형 예시다. 초기 제작 피드백에서 원하는 국소 밀도가 배경 장식·글리터 등으로 치환될 수 있다는 문제가 제기되어, 그 차이를 비교하기 위한 설계로 정리했다. **채택 화풍·고정 성공 프롬프트·검증된 모델 기제가 아니다.** 예시 이미지와 실험 결과 바이너리는 제공하지 않는다.

## 무엇을 원하고 무엇이 문제가 되었나

목표는 '배경에 기하학 장식을 뿌린 애니 그림'이 아니라 **인물의 셀채색 자체가 조각난 색면과 입자들로 고밀도 재구성되어 보이는 2D 그래픽 감각**이다. 얼굴의 정체성·표정·실루엣은 보존한다. 의도적으로 분해하는 곳과 그대로 남길 곳을 정한 뒤, 화면이 가득 차 보이는 복잡함 대신 **원하는 부분의 국소적 복잡함**을 강화한다.

1차 실패 가능성을 기정사실로 단정하지 않는다. 눈에 보이는 증상은 '요구한 조각/점의 밀도가 약함'이다. 후보 원인으로 배경 과잉·기하학 장식의 구분 실패·하이라이트로의 치환·스타일 참조의 영향·모델의 재해석을 따로 확인한다. 한 후보로 모델 내부의 원인을 확정하지 않는다.

## 표현 요소 5층

| 층 | 역할 | 강하게 표현할 곳 | 조용히 둘 곳 | 피해야 할 오독 |
|---|---|---|---|---|
| 1. 실루엣/선 | 애니풍 인물의 정체성과 표정, 포즈를 읽게 함 | 얼굴 윤곽, 눈, 손의 중요한 행동 | 부차적 옷 주름 | 뾰족한 조각 때문에 인물 외곽이 부서진 것처럼 보임 |
| 2. 기본 셀채색 | 그림이 여전히 2D 애니 셀화임을 보증 | 피부·얼굴·머리카락·옷의 큰 색/그림자 면 | 소재별 과도한 광택 | 3D 유리·보석·사진 합성으로 바뀜 |
| 3. 색면 파편 | 그림자 경계와 색 변화 자체가 해체·재조합되는 시각 보상 | 머리카락 그늘·옷깃·망토·어두운 색면 또는 지정 영역 | 표정의 핵심 미세 부위 | 배경에만 놓인 별/삼각형 스티커, 몸 외부에 떠 있는 파편 |
| 4. 점·망점·색 스패터 | 큰 조각 사이에 작은 조각들이 증식하는 조직감과 밀도 | 파편 경계 주변의 부분적 과밀 영역 | 시선·얼굴 중심·강한 주초점 주변 | 단순 글리터·보케·먼지·디지털 노이즈로 치환 |
| 5. 배경/여백 | 인물 내부 색채의 우글거림을 비교해 드러냄 | 정서를 전달할 정도의 빛·색·장소 단서 | 인물 채색과 경쟁하는 전면 패턴 | 배경이 더 복잡해져 주인공의 채색이 평범해짐 |

이것은 **일률적인 배경 단순화 명령이 아니다**. 배경 자체의 부서진 도시·환상적 공간이 보상인 장면이면 그 표현이 우선할 수 있다. 여기서 말하는 기본값은 이번 '캐릭터 채색의 파편화'를 분리 시험하기 위한 조건이다.

## 핵심 지시 언어

모델에게 작업 위치·방식·규모 변화·남길 기반을 구체적으로 적는다.

> 윤곽과 표정이 정확히 읽히는 2D 애니메이션 셀채색을 바탕으로 한다. 머리카락과 의상의 명암 경계를 따라 평평한 보라·자주·분홍·청록 계열 색면이 불규칙한 다각형 조각들로 갈라지고, 큰 색면에서 작은 색면을 거쳐 촘촘한 미세 색점·망점으로 이동한다. 이 분해는 공중에 떠 있는 장식보다 **인물 내부 채색의 일부**로 보이게 한다. 분해가 가장 밀집한 영역과 깨끗하게 남는 영역의 대비를 설계하고 얼굴과 핵심 제스처의 가독성을 지킨다. 배경의 그래픽 질감은 인물의 밀도와 경쟁하지 않는 수준으로 장면에 맞게 선택한다.

이는 실험용 지시문이지 기계적 보증이나 모든 작품에 적용할 공통 키워드가 아니다. 색 조합·인물·배경은 실제 대상에 따라 바뀐다. 반드시 보존해야 할 복장과 작품의 색은 임의 보색을 넣지 않는다.

## 구별할 네 가지 연출

**A. 셀채색 기준선:** 실루엣·인물 매력·기본 셀화만으로 목표 정서가 전달되는지 본다. 스타일 비교의 통제 조건이며 '최종 그림체'가 아니다.

**B. 색면 분할:** 그림자나 머리카락의 **색면 자체**가 각진 단편으로 이어지는가. 패턴이 배경 장식으로 밀려나지 않았는가.

**C. 국소 입자 밀도:** 작은 점·망점·스패터가 파편 경계에서 촘촘하게 나타나고 인물의 표현과 결합하는가. 빛 입자·보케·먼지만 늘어났는가.

**D. B+C 결합:** 큰 색면→작은 단편→미세 색점의 스케일 연속성이 한 영역 안에서 관찰되는가. 얼굴, 눈, 주된 제스처와의 위계가 살아 있는가.

처음부터 여러 다른 화면·조명·의상·카메라·도구 모델을 동시에 바꾸면 개선의 이유를 알 수 없다. 현재 도구가 여러 후보·참조를 지원하는 범위에서 A/B/C/D 중 필요한 비교만 한다. 사용자 요청이 1장이라면 4장을 몰래 생성하지 않는다. 별도 비교 없이 좋은 D 후보를 받았다면 사용자 선택을 존중하고 불필요한 재시험을 강제하지 않는다.

## 표현에 대한 진단 질문

- **정체성**: 얼굴·체형·의상 상태·핵심 실루엣이 이전 참조를 제대로 따르는가? 정체성 실패를 스타일 성과로 상쇄하지 않는다.
- **채색 위치**: 조각과 점이 캐릭터 *안쪽의 색 변화*인가, 배경/앞쪽 레이어에만 있는가?
- **우글거림의 형태**: 촘촘한 작은 색점과 중간 크기의 조각이 실제로 보이는가, 아니면 큰 삼각형 몇 개·유리 광택만 있는가?
- **국소 대비**: 가장 복잡한 부분과 쉬어 가는 면이 분명한가? 인물의 시선과 포즈를 해치지 않는가?
- **2D의 언어**: 셀화의 단단한 그림자 경계와 선을 지키는가, 수채/유화/3D 크리스털로 바뀌었는가?
- **장면의 감정**: 화면 전체 장식은 풍부한데 정작 예시 캐릭터가 전달할 정서가 약해진 것은 아닌가?

'성공'은 눈으로 관찰한 표현과 사용자 취향의 선택으로만 기록한다. 선택 후에는 좋은 부분(예: 눈과 얼굴, 특정 파편 대역)을 보존하며 부족한 층에만 수정한다. 매 실패마다 장문의 금지문을 추가하지 않는다.

## 캐릭터 일러스트에 쓸 수 있는 시험용 작화 문장

다음 문장은 **스타일 설계 예시**이며 실제 생성 지시·기존 시안의 재현 계약은 아니다. 구체적인 이야기 장면/인물 참조가 주어지면 거기에 맞게 바꾼다.

> 예시 캐릭터의 감정이 절제되어 있으나 시선과 자세에서 불안한 긴장이 읽히는 2D 셀화 일러스트. 머리카락과 검은 의상 안에서 보라·자주의 명암이 각진 색면으로 벌어지고, 특히 그림자 경계의 일부가 중소형 다각형과 아주 작은 점·망점으로 촘촘하게 분해된다. 얼굴의 눈·입과 의상 실루엣은 맑고 선명하게 남는다. 배경은 예시 캐릭터의 정서를 받쳐 주되 그래픽 파편 표현의 주된 무대가 되지 않으며, 화면의 가장 풍부한 미세 질감은 인물의 채색에서 발견된다. 시선·몸·중심 조명의 정확한 선택은 채택한 장면과 참조의 필수 관계를 지키는 범위에서 정한다.

**주의:** 정확한 악세서리·의상은 이미지/채택 정본 참조가 있을 때만 주장한다. 실제로 제공되지 않은 그림체 참조를 첨부했다고 말하지 않는다. 초기 방향성 피드백만으로 스타일 성공이나 실패 원인을 확정하지 않는다.


---

# 배포 라이선스 — CC BY-NC 4.0 표준 전문

Attribution-NonCommercial 4.0 International

=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
    wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public:
    wiki.creativecommons.org/Considerations_for_licensees

=======================================================================

Creative Commons Attribution-NonCommercial 4.0 International Public
License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution-NonCommercial 4.0 International Public License ("Public
License"). To the extent this Public License may be interpreted as a
contract, You are granted the Licensed Rights in consideration of Your
acceptance of these terms and conditions, and the Licensor grants You
such rights in consideration of benefits the Licensor receives from
making the Licensed Material available under these terms and
conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.

  c. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.
  d. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  e. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  f. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  g. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  h. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  i. NonCommercial means not primarily intended for or directed towards
     commercial advantage or monetary compensation. For purposes of
     this Public License, the exchange of the Licensed Material for
     other material subject to Copyright and Similar Rights by digital
     file-sharing or similar means is NonCommercial provided there is
     no payment of monetary compensation in connection with the
     exchange.

  j. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  k. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  l. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part, for NonCommercial purposes only; and

            b. produce, reproduce, and Share Adapted Material for
               NonCommercial purposes only.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties, including when
          the Licensed Material is used other than for NonCommercial
          purposes.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.

       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

       4. If You Share Adapted Material You produce, the Adapter's
          License You apply must not prevent recipients of the Adapted
          Material from complying with this Public License.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database for NonCommercial purposes
     only;

  b. if You include all or a substantial portion of the database
     contents in a database in which You have Sui Generis Database
     Rights, then the database in which You have Sui Generis Database
     Rights (but not its individual contents) is Adapted Material; and

  c. You must comply with the conditions in Section 3(a) if You Share
     all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not
replace Your obligations under this Public License where the Licensed
Rights include other Copyright and Similar Rights.


Section 5 -- Disclaimer of Warranties and Limitation of Liability.

  a. UNLESS OTHERWISE SEPARATELY UNDERTAKEN BY THE LICENSOR, TO THE
     EXTENT POSSIBLE, THE LICENSOR OFFERS THE LICENSED MATERIAL AS-IS
     AND AS-AVAILABLE, AND MAKES NO REPRESENTATIONS OR WARRANTIES OF
     ANY KIND CONCERNING THE LICENSED MATERIAL, WHETHER EXPRESS,
     IMPLIED, STATUTORY, OR OTHER. THIS INCLUDES, WITHOUT LIMITATION,
     WARRANTIES OF TITLE, MERCHANTABILITY, FITNESS FOR A PARTICULAR
     PURPOSE, NON-INFRINGEMENT, ABSENCE OF LATENT OR OTHER DEFECTS,
     ACCURACY, OR THE PRESENCE OR ABSENCE OF ERRORS, WHETHER OR NOT
     KNOWN OR DISCOVERABLE. WHERE DISCLAIMERS OF WARRANTIES ARE NOT
     ALLOWED IN FULL OR IN PART, THIS DISCLAIMER MAY NOT APPLY TO YOU.

  b. TO THE EXTENT POSSIBLE, IN NO EVENT WILL THE LICENSOR BE LIABLE
     TO YOU ON ANY LEGAL THEORY (INCLUDING, WITHOUT LIMITATION,
     NEGLIGENCE) OR OTHERWISE FOR ANY DIRECT, SPECIAL, INDIRECT,
     INCIDENTAL, CONSEQUENTIAL, PUNITIVE, EXEMPLARY, OR OTHER LOSSES,
     COSTS, EXPENSES, OR DAMAGES ARISING OUT OF THIS PUBLIC LICENSE OR
     USE OF THE LICENSED MATERIAL, EVEN IF THE LICENSOR HAS BEEN
     ADVISED OF THE POSSIBILITY OF SUCH LOSSES, COSTS, EXPENSES, OR
     DAMAGES. WHERE A LIMITATION OF LIABILITY IS NOT ALLOWED IN FULL OR
     IN PART, THIS LIMITATION MAY NOT APPLY TO YOU.

  c. The disclaimer of warranties and limitation of liability provided
     above shall be interpreted in a manner that, to the extent
     possible, most closely approximates an absolute disclaimer and
     waiver of all liability.


Section 6 -- Term and Termination.

  a. This Public License applies for the term of the Copyright and
     Similar Rights licensed here. However, if You fail to comply with
     this Public License, then Your rights under this Public License
     terminate automatically.

  b. Where Your right to use the Licensed Material has terminated under
     Section 6(a), it reinstates:

       1. automatically as of the date the violation is cured, provided
          it is cured within 30 days of Your discovery of the
          violation; or

       2. upon express reinstatement by the Licensor.

     For the avoidance of doubt, this Section 6(b) does not affect any
     right the Licensor may have to seek remedies for Your violations
     of this Public License.

  c. For the avoidance of doubt, the Licensor may also offer the
     Licensed Material under separate terms or conditions or stop
     distributing the Licensed Material at any time; however, doing so
     will not terminate this Public License.

  d. Sections 1, 5, 6, 7, and 8 survive termination of this Public
     License.


Section 7 -- Other Terms and Conditions.

  a. The Licensor shall not be bound by any additional or different
     terms or conditions communicated by You unless expressly agreed.

  b. Any arrangements, understandings, or agreements regarding the
     Licensed Material not stated herein are separate from and
     independent of the terms and conditions of this Public License.


Section 8 -- Interpretation.

  a. For the avoidance of doubt, this Public License does not, and
     shall not be interpreted to, reduce, limit, restrict, or impose
     conditions on any use of the Licensed Material that could lawfully
     be made without permission under this Public License.

  b. To the extent possible, if any provision of this Public License is
     deemed unenforceable, it shall be automatically reformed to the
     minimum extent necessary to make it enforceable. If the provision
     cannot be reformed, it shall be severed from this Public License
     without affecting the enforceability of the remaining terms and
     conditions.

  c. No term or condition of this Public License will be waived and no
     failure to comply consented to unless expressly agreed to by the
     Licensor.

  d. Nothing in this Public License constitutes or may be interpreted
     as a limitation upon, or waiver of, any privileges and immunities
     that apply to the Licensor or You, including from the legal
     processes of any jurisdiction or authority.

=======================================================================

Creative Commons is not a party to its public
licenses. Notwithstanding, Creative Commons may elect to apply one of
its public licenses to material it publishes and in those instances
will be considered the “Licensor.” The text of the Creative Commons
public licenses is dedicated to the public domain under the CC0 Public
Domain Dedication. Except for the limited purpose of indicating that
material is shared under a Creative Commons public license or as
otherwise permitted by the Creative Commons policies published at
creativecommons.org/policies, Creative Commons does not authorize the
use of the trademark "Creative Commons" or any other trademark or logo
of Creative Commons without its prior written consent including,
without limitation, in connection with any unauthorized modifications
to any of its public licenses or any other arrangements,
understandings, or agreements concerning use of licensed material. For
the avoidance of doubt, this paragraph does not form part of the
public licenses.

Creative Commons may be contacted at creativecommons.org.



---

# IGP — Additional Permission and Attribution Waiver

Copyright (c) 2026 Q0916

Effective date: 2026-10-21

The Image Generation Principles (IGP) instructions, documentation, reference text,
and distributable copies authored and supplied by Q0916 in this repository (the
"Material") are licensed under Creative Commons Attribution-NonCommercial 4.0
International (CC BY-NC 4.0). The unmodified standard legal code is in LICENSE.md:
https://creativecommons.org/licenses/by-nc/4.0/

To the extent Q0916 holds the relevant rights, Q0916 grants everyone the following
waiver and additional permissions. These are separate grants by Q0916, not changes
to the Creative Commons legal code and not terms authored by Creative Commons.

## 1. Attribution is optional

Q0916 waives the requirements to credit Q0916 or IGP, retain a copyright notice
naming Q0916, link to the original source, or identify modifications. This waiver
applies to use, copying, modification, translation, and redistribution of the
Material and adaptations, as well as to resulting creative work.

The CC license and warranty-disclaimer notices remain applicable to copies of the
Material. No visible IGP credit or license notice is required on creative outputs
merely because IGP was used to make them. Third-party attribution requirements
are not waived by Q0916.

## 2. Commercial use and free sharing are permitted

In addition to the rights granted by CC BY-NC 4.0, you may use, reproduce, modify,
and translate the Material as a tool in personal, professional, and commercial
workflows. This expressly includes supplying it as instructions or context to an
AI model, doing paid or client work with its assistance, and selling or otherwise
commercially using resulting images, illustrations, and other creative outputs.

You may also redistribute the Material or adaptations free of charge, including
on a commercial or advertising-supported website or through a business, provided
access to those copies is not a paid item or paid access benefit. When relying on
these additional permissions to redistribute copies, include this permission
notice and the CC license notice so recipients can understand their permissions.
You do not need to add a separate creator credit or source link.

## 3. No permission to sell the skill itself

The additional commercial permission does not authorize selling, renting,
licensing for a fee, or charging for access to the Material or adaptations as a
paid item or paid access benefit. This includes paid prompt or skill packs,
bundles, subscription libraries, and paywalled downloads containing substantial
portions of the Material's protected expression. Renaming, translating,
reformatting, or editing those portions does not by itself make such resale
permitted. Separate permission from Q0916 is required for such distribution
unless it is already permitted by applicable law or the standard CC license.

Creative outputs do not become subject to IGP's license merely because IGP helped
create them. Copying substantial protected IGP text into a paid product and
calling it an output does not qualify for the commercial-production permission.

## 4. Scope of these grants

These grants are worldwide, royalty-free, nonexclusive, and irrevocable for uses
within their scope. They add permissions and waive conditions; they do not
restrict rights already granted by CC BY-NC 4.0 or by applicable exceptions and
limitations. Its remaining terms, including warranty and liability provisions,
continue to apply. If you do not rely on an additional permission, the standard
CC license remains independently available, with the attribution waiver above.

These grants do not relicense third-party works or linked resources, guarantee
rights in model outputs, or override applicable provider terms. They do not
restrict ideas, facts, general artistic knowledge, or independently created
instructions that do not copy the Material's protected expression. No endorsement
or trademark rights are granted.

---

한국어 요약: 출처 표시 없이 IGP를 사용·수정·번역하고 무료로 공유할 수 있습니다.
회사 업무·유료 의뢰·상업적 제작에 활용하거나 완성 이미지와 작업물을 판매해도
됩니다. IGP 자체나 그 원문을 상당 부분 담은 수정본·번역본을 유료 스킬팩,
구독 자료실, 유료 다운로드 등으로 재판매하는 허락은 포함하지 않습니다.
스킬 사본에는 라이선스 안내를 남기되 별도의 작가 크레딧은 요구하지 않습니다.
이 문서는 표준 CC 본문을 고친 라이선스가 아니라 Q0916의 별도 허용·면제입니다.
요약과 본문이 다르면 위 영문 본문을 따릅니다.

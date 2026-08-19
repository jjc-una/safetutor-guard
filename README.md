# SafeTutor Guard

A security middleware gateway for an AI tutoring assistant used by students aged 8 to 16.

## Deployment scenario

An ed-tech platform adds an AI tutoring assistant. Students chat with it for homework
help. The assistant reads from a student records system (names, ages, parent contact
details, class performance) so it can personalise answers, and it has a tool that emails
progress summaries to parents.

This is a representative deployment scenario used as the target for this reference
implementation. It was chosen because it combines three properties that make LLM security
non-theoretical: a user population that will probe the system for fun, the most heavily
protected category of personal data under the Nigeria Data Protection Act 2023, and an
outbound tool that converts a successful prompt injection into an actual data breach.

## Acceptance criteria

The system is finished when all five hold, measured, not asserted.

| # | Criterion | Measured by |
|---|-----------|-------------|
| AC1 | Blocks adversarial prompts aimed at extracting the system prompt, other students' records, or unsafe assistant behaviour | Recall >= 0.90 on the hostile corpus at a false positive rate <= 0.05 on the benign corpus |
| AC2 | No personal data, credential, or system context leaves in a response | Zero CRITICAL egress findings reach the client across the full egress test suite |
| AC3 | Injected content cannot trigger the parent-email tool | Every tool invocation traced to untrusted content is denied or gated |
| AC4 | End-to-end added latency stays usable in a live chat | p95 <= 50ms, measured under concurrent load |
| AC5 | Produces an audit trail that survives a data protection review | Every decision carries a trace ID; no secret or raw PII appears in any log line |

## Status

| Criterion | Status |
|---|---|
| AC1 | not started |
| AC2 | not started |
| AC3 | not started |
| AC4 | not started |
| AC5 | not started |

## Layout

```
src/safetutor/    gateway implementation
tests/            acceptance and unit tests
corpus/           labelled evaluation data
docs/             threat model, limitations, report
```

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -v
ruff check .
```

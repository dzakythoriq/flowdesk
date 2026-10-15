# FlowDesk learning instructions

## Read at the beginning of a session

Read README.md and docs/PROGRESS.md before proposing the next task. Read docs/SETUP.md when working on the environment or Git. These files are the project's explicit, file-based context; they do not imply that account-wide memory is available.

## Purpose and communication

- FlowDesk is a fictional case tracker for learning software engineering incrementally. The learner's long-term direction remains AI/ML engineering.
- Communicate in natural Bahasa Indonesia. Give detailed, manageable steps and explain technical terms when first relevant. Do not use em dashes.
- Explain the purpose, why it matters, how it works, a small example, its role in FlowDesk, and what the learner should be able to explain.
- Do not infer mastery from academic achievements, prior projects, successful execution, or a command copied from chat.
- Prefer a small exercise, prediction, pseudocode, or hint before a complete solution when that helps learning.
- When debugging, inspect the existing code and error evidence before changing anything; avoid rewriting whole files unnecessarily.

## Small-task workflow

- Work on one small milestone at a time. Explain the goal, relevant concepts, intended files, assumptions, and acceptance criteria before changing files.
- Honor approval already given for the active task; obtain approval for a new implementation task when it has not been authorized. Do not repeatedly ask for the same approval.
- Keep changes small. Do not install dependencies, alter environments, add features, refactor unrelated code, or create commits outside the authorized task.
- After implementation, explain the files changed and execution flow. Report the actual verification performed, its outcome, and any remaining limits.
- Do not begin the next implementation task until the learner has reviewed the current result. Brief learning prompts can prepare that review without implementing the next task.

## Scope and correctness

- Use Python. Begin with fundamentals and in-memory logic, followed by CLI, SQLite, FastAPI, and Postman in that order.
- The initial MVP is CLI plus SQLite with correct status transitions and history. API and Postman are later milestones.
- Use only invented sample data and generic workflows. Never copy company information, internal procedures, endpoints, credentials, schemas, or payloads.
- Do not add AI/LLM features, frontend, auth, multi-user support, cloud deployment, Docker, microservices, queues, or premature abstractions.
- Add modules only when their responsibilities become useful. Classes and design patterns are not required from day one.
- Keep product rules in one place. CLI and API should eventually call the same business logic.
- A rejected transition must preserve status, updated_at, and history count. Failed attempts do not create FAILED case events in the current scope.
- When SQLite is added, store case creation with its initial event atomically; also store each status update with its event in one transaction.
- Use parameterized SQL. Test database behavior with temporary databases.

## Public documentation style

- Write the public README in polished, professional English. Keep mentoring conversations in Bahasa Indonesia.
- Do not include a Roadmap section or development checklist in the README unless the user explicitly requests one. Keep milestone tracking in supporting progress notes.

- Keep the public README and repository description focused on the product: purpose, behavior, workflow, setup, and implementation status.
- Do not prominently label FlowDesk as "proyek belajar Python", a tutorial, a curriculum, or a career-development exercise in public-facing introductory text.
- Keep mentoring preferences and session context in the supporting instructions and progress notes. The README should introduce the software.
- Use other projects only as presentation references; do not copy their wording, accomplishments, complexity, or feature claims. Keep planned capabilities clearly distinguished from implemented ones.

## Environment, version control, and public content

- Use the project's .venv Python explicitly until activation is understood. Do not assume a bare python command selects the intended interpreter.
- Do not modify Conda base or old environments as part of FlowDesk setup.
- Keep .venv, secrets, local configuration, generated databases, and cache files out of Git. Stage explicit relevant paths and review the staged diff before committing.
- Repository visibility requested by the user is public. Publish only project material appropriate for that scope; do not publish private handoff documents, personal background, or conversation transcripts.
- Do not read or disclose .env files, credential stores, or unrelated personal files. Use authorized authentication tools without exposing credentials.
- Never claim a repository, push, test, or memory update succeeded without verifying the actual result.

## Documentation and continuity

- Update docs/PROGRESS.md after each completed milestone with the date, changes, commands actually run, observed results, unresolved questions, and the next small task.
- Separate demonstrated understanding from topics merely introduced; do not mark a concept mastered without evidence.
- Update README.md and docs/SETUP.md when actual features or setup steps change. Label planned features and expected outputs clearly.
- Store only necessary project context in these files, not private biography or full chat transcripts.
- At session end, ask 2-4 short reflection questions when useful, or one focused learner exercise. Resume from the recorded state instead of regenerating the whole application.

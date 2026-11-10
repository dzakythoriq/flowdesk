# FlowDesk

**Workflow Case Tracker & Simulator**

FlowDesk is designed to track cases through explicit status transitions, automatically generated identifiers, and a traceable event history. Its core focus is keeping each case's current state consistent with its recorded changes.

## Development Status

**Early development.** `create_case(title, description="")` requires a string title, raising `TypeError` for other types. It trims leading and trailing whitespace and rejects a blank result with `ValueError`. The description is optional and defaults to an empty string. When supplied, it must be a string. Valid input produces an independent in-memory case dictionary with the normalized title, supplied description, and an initial status of `NEW`. The script also supports status display and retrieval, and guarded opening from `NEW` to `OPEN`. `open_case(case_data)` uses the boolean result returned by `is_new_case(case_data)` to decide whether to update the supplied dictionary. It returns `True` after a successful opening and `False` when the attempt is rejected. Other starting statuses remain unchanged. The complete workflow, interactive CLI, event history, persistence layer, and API are not yet implemented.

## Planned Capabilities

- Create cases with an automatically generated ID, title, description, and timestamps.
- List cases and retrieve individual case details by ID.
- Validate status changes against explicit workflow rules.
- Record case creation and successful status changes in an event history.
- Persist case data locally using SQLite.
- Provide a CLI and, subsequently, a REST API backed by the same core operations.

A typical workflow starts with an operator creating a case such as `Review sample invoice`, opening it, starting work, and eventually resolving and closing it. Work can move to `BLOCKED` when an issue prevents progress, then return to `IN_PROGRESS` once the issue is cleared. All sample cases use fictional data.

## Workflow

The primary lifecycle is:

```text
NEW -> OPEN -> IN_PROGRESS -> RESOLVED -> CLOSED
```

| Current status | Allowed transitions |
|---|---|
| `NEW` | `OPEN`, `CANCELLED` |
| `OPEN` | `IN_PROGRESS`, `CANCELLED` |
| `IN_PROGRESS` | `BLOCKED`, `RESOLVED` |
| `BLOCKED` | `IN_PROGRESS` |
| `RESOLVED` | `CLOSED` |
| `CLOSED` | None |
| `CANCELLED` | None |

A rejected transition must leave the case's status, `updated_at`, and event history unchanged. Once persistence is implemented, case creation and status updates must be saved in the same database transaction as their corresponding history events.

## Data Model

| Entity | Planned fields |
|---|---|
| `Case` | `case_id`, `title`, `description`, `status`, `created_at`, `updated_at` |
| `CaseEvent` | `event_id`, `case_id`, `event_type`, `old_status`, `new_status`, `reason`, `created_at` |

`Case` stores the current state. `CaseEvent` records an event associated with a case. The initial event types are `CASE_CREATED` and `STATUS_CHANGED`.

## Technology

| Component | Technology | Status |
|---|---|---|
| Runtime | Python 3.14 | Environment configured |
| Persistence | SQLite via `sqlite3` | Planned |
| API | FastAPI | Planned |
| Automated testing | pytest | Planned |

## Setup

See the [setup guide](docs/SETUP.md) for local environment configuration. If `.venv` already exists, run the following checks from the repository root in PowerShell:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
.\.venv\Scripts\python.exe -m pip --version
```

The interpreter and pip paths should point to this project's `.venv` directory. The virtual environment check should return `True`.

Run the current case-state script from the repository root:

```powershell
.\.venv\Scripts\python.exe main.py
```

The sample creates two cases with different titles and descriptions through `create_case`, then prints both dictionaries before any opening attempt. It stores the operation results of two opening attempts on the first case and uses a conditional in the caller to print a success or rejection message for each result. It then attempts to open that case once more, displays both case statuses, opens the second case, and checks the first case's returned status before printing a readiness message. The first title includes outer spaces that are removed before storage. A final example omits the description and prints the newly created case with its default empty description. Its caller also handles validation errors with `try/except`:

```text
{'title': 'Review sample invoice', 'description': 'Fictional invoice', 'status': 'NEW'}
{'title': 'Check sample delivery', 'description': 'Fictional delivery', 'status': 'NEW'}
The case was opened successfully
The case was not opened successfully
OPEN
NEW
OPEN
OPEN
This case is ready for processing
{'title': 'Review invoice', 'description': '', 'status': 'NEW'}
Validation check completed
```

`is_new_case(case_data)` returns a boolean without printing or modifying the case. `open_case(case_data)` uses that predicate directly as its condition, updates the supplied dictionary only when allowed, and returns whether that opening attempt succeeded. Repeated attempts on an `OPEN` case leave it unchanged. The sample stores the first two operation results in `opening_succeeded` and `second_opening_succeeded`. These booleans describe individual attempts; the case dictionary separately stores the current status. `open_case` does not print messages; the caller chooses how to present each result. A direct call still applies the opening rule even when its return value is not displayed.

`create_case` returns a new dictionary for each valid call without printing. It checks the title type before applying `title.strip()`, preserving whitespace between words. Non-string titles raise `TypeError`; empty or whitespace-only strings raise `ValueError`, both before dictionary creation. For example, the integer `123` is rejected, while the non-blank string `"123"` is accepted. The caller handles each error type with a corresponding `except` clause and displays a short message. Non-string descriptions also raise `TypeError`. Call `create_case(title)` to use the default empty description, or pass a string as the second argument to supply one. Generated identifiers and timestamps are not yet implemented. Opening one case leaves the other case unchanged. Sample data is held in memory and recreated on each run.

A persistent automated test suite is not yet available.

## Scope

The initial version targets a single local operator working with fictional data. A web frontend, authentication, multi-user support, notifications, external integrations, AI/LLM features, and cloud deployment are outside the initial scope.

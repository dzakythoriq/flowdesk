# FlowDesk

**Workflow Case Tracker & Simulator**

FlowDesk is designed to track cases through explicit status transitions, automatically generated identifiers, and a traceable event history. Its core focus is keeping each case's current state consistent with its recorded changes.

## Development Status

**Early development.** A minimal in-memory script uses separate functions to display a case's status and open it. Opening is allowed only from `NEW` to `OPEN`; other starting statuses remain unchanged. The complete workflow, interactive CLI, event history, persistence layer, and API are not yet implemented.

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

The script uses the sample case defined in `main.py`. `show_status(case_data)` displays its current status, and `open_case(case_data)` opens it only when its status is `NEW`. The sample calls these functions to display the status before and after the opening attempt:

```text
NEW
This case is new
OPEN
```

Other starting statuses remain unchanged. Repeating the opening attempt on an `OPEN` case also leaves its status unchanged. The script operates in memory and recreates the sample data on each run.

A persistent automated test suite is not yet available.

## Scope

The initial version targets a single local operator working with fictional data. A web frontend, authentication, multi-user support, notifications, external integrations, AI/LLM features, and cloud deployment are outside the initial scope.

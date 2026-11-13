# FlowDesk

**Workflow Case Tracker & Simulator**

FlowDesk is designed to track cases through explicit status transitions, automatically generated identifiers, and a traceable event history. Its core focus is keeping each case's current state consistent with its recorded changes.

## Capabilities

`create_case(title, description="")` requires a string title, raising `TypeError` for other types. It trims leading and trailing whitespace and rejects a blank result with `ValueError`. The description is optional and defaults to an empty string. When supplied, it must be a string. Valid input produces an independent in-memory case dictionary with a generated `CASE-` prefixed UUIDv4, the normalized title, the supplied description, and an initial status of `NEW`. The script supports status display and retrieval and validates transitions against the workflow table below. `transition_case(case_data, new_status)` returns `True` after an allowed update and `False` when the attempt is rejected, leaving the case unchanged. `open_case(case_data)` delegates to that function with `OPEN` as the target. Each case records UTC creation and update timestamps and an in-memory history of creation and successful status changes. The terminal menu supports creating and listing cases, retrieving case details, changing status, and viewing event history. Details, status changes, and history are accessed by case ID. Case creation saves the case and its initial event together in SQLite. The terminal menu loads saved cases and their event history from SQLite at startup. Successful status changes and their events are also persisted together. The API creates cases, retrieves case lists, details, and event history, and applies status changes using the same SQLite database.

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

A rejected transition leaves the case's status, `updated_at`, and event history unchanged. Case creation and each successful status change are stored in the same transaction as the corresponding event. If an event cannot be saved, its case creation or status update is rolled back.

## Data Model

| Entity | Fields |
|---|---|
| `Case` | `case_id`, `title`, `description`, `status`, `created_at`, `updated_at` |
| `CaseEvent` | `event_id`, `case_id`, `event_type`, `old_status`, `new_status`, `reason`, `created_at` |

`Case` stores the current state. `CaseEvent` records an event associated with a case. The initial event types are `CASE_CREATED` and `STATUS_CHANGED`.

## Technology

| Component | Technology | Status |
|---|---|---|
| Runtime | Python 3.14 | Environment configured |
| Persistence | SQLite via `sqlite3` | Implemented for case creation, status changes, and history |
| API | FastAPI | Case creation, listing, details, history, and status changes implemented |
| Automated testing | pytest and FastAPI TestClient | Workflow, persistence, rollback, and HTTP responses covered |

## Setup

See the [setup guide](docs/SETUP.md) for local environment configuration. If `.venv` already exists, run the following checks from the repository root in PowerShell:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)"
.\.venv\Scripts\python.exe -m pip --version
```

The interpreter and pip paths should point to this project's `.venv` directory. The virtual environment check should return `True`.

Start the terminal menu from the repository root. It initializes the database if needed:

```powershell
.\.venv\Scripts\python.exe main.py
```

Choose `1` to create a case and `2` to list cases. Enter a case ID in options `3`, `4`, or `5` to view details, change status, or view event history, respectively. Choose `0` to exit. Press Enter at the description prompt to leave it empty. The menu reports a blank title and returns to the choices without storing a case. A valid creation prints its generated ID; the list shows each ID, current status, and title.

```text
Choose an option: 1
Title: Review sample invoice
Description (optional):
Created: CASE-<uuid>
```

`transition_case` reads the current status, looks up the allowed destinations, and updates only the supplied case when the target is allowed. `open_case(case_data)` forwards the result of `transition_case(case_data, "OPEN")`. Neither function prints; the caller chooses how to present the result. The case dictionary stores the current status separately from the boolean result of each attempt. Its `history` list starts with `CASE_CREATED`; each allowed transition appends one `STATUS_CHANGED` event with the previous and new status, optional reason, and UTC timestamp. The case’s `updated_at` matches its latest event time.

`create_case` returns a new dictionary for each valid call without printing. It checks the title type before applying `title.strip()`, preserving whitespace between words. Non-string titles raise `TypeError`; empty or whitespace-only strings raise `ValueError`, both before dictionary creation. For example, the integer `123` is rejected, while the non-blank string `"123"` is accepted. The caller handles each error type with a corresponding `except` clause and displays a short message. Non-string descriptions also raise `TypeError`. Call `create_case(title)` to use the default empty description, or pass a string as the second argument to supply one. Opening one case leaves the other case unchanged. Saved cases, current statuses, and event history are available when FlowDesk is reopened.

## Run the API locally

```powershell
.\.venv\Scripts\python.exe -m pip install fastapi uvicorn
.\.venv\Scripts\python.exe -m uvicorn api:app --reload
```

Open [the case list](http://127.0.0.1:8000/cases) to retrieve each case's ID, title, and current status. Request `GET /cases/{case_id}` for one case's details, including its description and timestamps. Request `GET /cases/{case_id}/history` for the case's chronological event history. An unknown ID returns `404 Not Found`. Use `POST /cases` with a required title and an optional description to create a case. A successful request returns `201 Created`. Use `PATCH /cases/{case_id}/status` with a required `new_status` and optional `reason`. A successful transition returns `200 OK`. An unknown status returns `422`, and a disallowed transition returns `409 Conflict`. The endpoints are available in the [interactive API documentation](http://127.0.0.1:8000/docs).

## Tests

Install the API and test dependencies in the project environment, then run the suite from the repository root:

```powershell
.\.venv\Scripts\python.exe -m pip install fastapi uvicorn pytest httpx2
.\.venv\Scripts\python.exe -m pytest -q
```

The suite includes 3 storage and workflow checks and 12 API checks. API tests use FastAPI's TestClient and temporary SQLite databases. They cover case creation, listing, details, history, status changes, and responses for invalid requests, missing cases, and disallowed transitions.

## Postman demo

Import the [FlowDesk collection](postman/FlowDesk.postman_collection.json) into Postman and run it in order against the local API. It creates a fictional case, uses the returned ID in later requests, opens the case, and verifies that an invalid transition leaves the status and history intact. Each run creates a new sample case.

With Postman CLI installed and the API running locally, run the collection from the repository root.

```powershell
postman collection run ./postman/FlowDesk.postman_collection.json
```

## Scope

The initial version targets a single local operator working with fictional data. A web frontend, authentication, multi-user support, notifications, external integrations, AI/LLM features, and cloud deployment are outside the initial scope.

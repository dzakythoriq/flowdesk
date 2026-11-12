import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("flowdesk.db")

def init_db():
    connection = sqlite3.connect(DB_PATH)

    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("""
            CREATE TABLE IF NOT EXISTS cases (
                case_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        connection.execute("""
            CREATE TABLE IF NOT EXISTS case_events (
                event_id TEXT PRIMARY KEY NOT NULL,
                case_id TEXT NOT NULL,
                event_type TEXT NOT NULL,
                old_status TEXT,
                new_status TEXT NOT NULL,
                reason TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY (case_id) REFERENCES cases(case_id)
            )
        """)
        connection.commit()
    finally:
        connection.close()
            
def save_case(case_data):
    event = case_data["history"][-1]  # Get the most recent event
    connection = sqlite3.connect(DB_PATH)
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        with connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO cases (case_id, title, description, status, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    case_data["case_id"],
                    case_data["title"],
                    case_data["description"],
                    case_data["status"],
                    case_data["created_at"],
                    case_data["updated_at"],
                ),
            )
            connection.execute(
                """
                INSERT INTO case_events
                    (event_id, case_id, event_type, old_status, new_status, reason, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event["event_id"],
                    event["case_id"],
                    event["event_type"],
                    event.get("old_status"),
                    event["new_status"],
                    event.get("reason"),
                    event["created_at"],
                ),
            )
    finally:
        connection.close()
    
def load_cases():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    try:
        connection.execute("BEGIN")
        cases_by_id = {}

        for row in connection.execute("SELECT * FROM cases ORDER BY created_at, case_id"):
            case_data = dict(row)
            case_data["history"] = []
            cases_by_id[case_data["case_id"]] = case_data

        for row in connection.execute("SELECT * FROM case_events ORDER BY created_at, rowid"):
            cases_by_id[row["case_id"]]["history"].append(dict(row))

        return cases_by_id
    finally:
        connection.close()
        
def _insert_event(connection, event):
    connection.execute(
        """
        INSERT INTO case_events
            (event_id, case_id, event_type, old_status, new_status, reason, created_at)
        VALUES
            (:event_id, :case_id, :event_type, :old_status, :new_status, :reason, :created_at)
        """,
        event,
    )


def save_status_change(case_data):
    event = case_data["history"][-1]
    connection = sqlite3.connect(DB_PATH)

    try:
        connection.execute("PRAGMA foreign_keys = ON")
        with connection:
            connection.execute("BEGIN")
            result = connection.execute(
                """
                UPDATE cases SET status = ?, updated_at = ?
                WHERE case_id = ? AND status = ?
                """,
                (
                    event["new_status"],
                    event["created_at"],
                    event["case_id"],
                    event["old_status"],
                ),
            )
            if result.rowcount != 1:
                raise sqlite3.IntegrityError("Case status no longer matches")

            _insert_event(connection, event)
    finally:
        connection.close()
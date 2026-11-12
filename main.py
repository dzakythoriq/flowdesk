from uuid import uuid4
from datetime import datetime, timezone
import sqlite3
from storage import init_db, load_cases, save_case, save_status_change
from copy import deepcopy

ALLOWED_TRANSITIONS = {
    "NEW": ["OPEN", "CANCELLED"],
    "OPEN": ["IN_PROGRESS", "CANCELLED"],
    "IN_PROGRESS": ["BLOCKED", "RESOLVED"],
    "BLOCKED": ["IN_PROGRESS"],
    "RESOLVED": ["CLOSED"],
    "CLOSED": [],
    "CANCELLED": [],
}

def make_event(case_id, event_type, old_status, new_status, reason=None):
    return {
        "event_id": "EVENT-" + str(uuid4()),
        "case_id": case_id,
        "event_type": event_type,
        "old_status": old_status,
        "new_status": new_status,
        "reason": reason,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

def transition_case(case_data, new_status, reason=None):
    current_status = case_data["status"]
    allowed_statuses = ALLOWED_TRANSITIONS.get(current_status, [])

    if new_status not in allowed_statuses:
        return False

    event = make_event(
        case_data["case_id"], "STATUS_CHANGED", current_status, new_status, reason
    )
    case_data["status"] = new_status
    case_data["updated_at"] = event["created_at"]
    case_data["history"].append(event)
    return True

def show_status(case_data):
    print(case_data["status"])
    

def open_case(case_data):
    return transition_case(case_data, "OPEN")    

def get_status(case_data):
    return case_data["status"]

def is_new_case(case_data):
    return case_data["status"] == "NEW"

def create_case(title,description=""):
    if not isinstance(title, str):
        raise TypeError("Title must be a string")
    
    title = title.strip()
    
    if title == "":
        raise ValueError("Title cannot be empty")

    if not isinstance(description, str):
        raise TypeError("Description must be a string")
    
    case_id = "CASE-" + str(uuid4())
    
    created_event = make_event(case_id, "CASE_CREATED", None, "NEW")
    
    case_data = {
        "created_at": created_event["created_at"],
        "updated_at": created_event["created_at"],
        "history": [created_event],
        "case_id": case_id,
        "title": title,
        "description": description,
        "status": "NEW"
    }
    return case_data

def run_cli():
    init_db()
    cases_by_id = load_cases()

    while True:
        print("\n1. Create case\n2. List cases\n3. Show case detail")
        print("4. Change case status\n5. View case history\n0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice == "1":
            title = input("Title: ")
            description = input("Description (optional): ")

            try:
                case_data = create_case(title, description)
                save_case(case_data)
            except ValueError as error:
                print("Error:", error)
                continue
            except sqlite3.Error as error:
                print("Error saving case:", error)
                continue

            cases_by_id[case_data["case_id"]] = case_data
            print("Created:", case_data["case_id"])

        elif choice == "2":
            if not cases_by_id:
                print("No cases yet.")

            for case_data in cases_by_id.values():
                print(case_data["case_id"], "|", case_data["status"], "|", case_data["title"])
                
        elif choice in ("3", "4", "5"):
            case_id = input("Case ID: ").strip()
            case_data = cases_by_id.get(case_id)

            if case_data is None:
                print("Error: Case not found.")
                continue

            if choice == "3":
                for field in ("case_id", "title", "description", "status", "created_at", "updated_at"):
                    print(field + ":", case_data[field])

            elif choice == "4":
                current_status = case_data["status"]
                print("Allowed next statuses:", ALLOWED_TRANSITIONS[current_status])
                new_status = input("New status: ").strip().upper()

                if new_status not in ALLOWED_TRANSITIONS:
                    print("Error: Unknown status.")
                    continue

                reason = input("Reason (optional): ").strip() or None
                updated_case = deepcopy(case_data)
                
                if not transition_case(updated_case, new_status, reason):
                    print("Error: Cannot move from", current_status, "to", new_status)
                    continue

                try:
                    save_status_change(updated_case)
                except sqlite3.Error as error:
                    print("Error saving status:", error)
                    continue

                cases_by_id[case_id] = updated_case
                print("Updated:", updated_case["status"])

            else:
                for event in case_data["history"]:
                    print(
                        event["created_at"],
                        event["event_type"],
                        event["old_status"], "->", event["new_status"],
                        "| Reason:", event["reason"],
                    )        
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_cli()
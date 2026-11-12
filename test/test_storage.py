import storage
from main import create_case, transition_case
import sqlite3
from copy import deepcopy

import pytest


def test_saved_status_and_history_can_be_loaded(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DB_PATH", tmp_path / "flowdesk.db")
    storage.init_db()

    case = create_case("Sample invoice")
    storage.save_case(case)

    assert transition_case(case, "OPEN", "Ready for review") is True
    storage.save_status_change(case)

    loaded_case = storage.load_cases()[case["case_id"]]

    assert loaded_case["status"] == "OPEN"
    assert [event["event_type"] for event in loaded_case["history"]] == [
        "CASE_CREATED",
        "STATUS_CHANGED",
    ]
    assert loaded_case["history"][-1]["reason"] == "Ready for review"
    
def test_illegal_transition_keeps_case_unchanged():
    case = create_case("Sample invoice")
    assert transition_case(case, "OPEN") is True
    before = deepcopy(case)

    assert transition_case(case, "CLOSED") is False
    assert case == before
    
def test_event_insert_failure_rolls_back_status(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DB_PATH", tmp_path / "flowdesk.db")
    storage.init_db()

    case = create_case("Sample invoice")
    storage.save_case(case)
    case_id = case["case_id"]
    before = storage.load_cases()[case_id]

    assert transition_case(case, "OPEN") is True
    case["history"][-1]["event_id"] = before["history"][0]["event_id"]

    with pytest.raises(sqlite3.IntegrityError, match="case_events.event_id"):
        storage.save_status_change(case)

    assert storage.load_cases()[case_id] == before
import pytest
from fastapi.testclient import TestClient

import storage
from api import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DB_PATH", tmp_path / "flowdesk.db")
    with TestClient(app) as test_client:
        yield test_client


def test_case_lifecycle(client):
    initial_list = client.get("/cases")
    assert initial_list.status_code == 200
    assert initial_list.json() == []

    response = client.post("/cases", json={"title": "  Review sample invoice  "})
    assert response.status_code == 201
    case = response.json()
    case_id = case["case_id"]
    path = f"/cases/{case_id}"
    assert case_id.startswith("CASE-")
    assert case["title"] == "Review sample invoice"
    assert case["description"] == ""
    assert case["status"] == "NEW"

    history = client.get(f"{path}/history")
    assert history.status_code == 200
    assert [
        (event["event_type"], event["old_status"], event["new_status"])
        for event in history.json()
    ] == [("CASE_CREATED", None, "NEW")]

    response = client.patch(
        f"{path}/status", json={"new_status": "open", "reason": "Ready for review"}
    )
    assert response.status_code == 200
    updated = response.json()
    assert updated["status"] == "OPEN"

    response = client.get("/cases")
    assert response.status_code == 200
    assert response.json() == [
        {"case_id": case_id, "title": "Review sample invoice", "status": "OPEN"}
    ]

    response = client.get(path)
    assert response.status_code == 200
    assert response.json() == {
        **case, "status": "OPEN", "updated_at": updated["updated_at"]
    }

    response = client.get(f"{path}/history")
    assert response.status_code == 200
    events = response.json()
    assert [event["event_type"] for event in events] == ["CASE_CREATED", "STATUS_CHANGED"]
    assert all(event["case_id"] == case_id for event in events)
    assert events[-1]["old_status"] == "NEW"
    assert events[-1]["new_status"] == "OPEN"
    assert events[-1]["reason"] == "Ready for review"
    assert events[-1]["created_at"] == updated["updated_at"]


@pytest.mark.parametrize(
    "payload",
    [{}, {"title": "   "}, {"title": 123}, {"title": "Sample", "status": "OPEN"}],
)
def test_invalid_create_keeps_database_empty(client, payload):
    response = client.post("/cases", json=payload)
    assert response.status_code == 422
    assert client.get("/cases").json() == []


@pytest.mark.parametrize(
    ("method", "path", "options"),
    [
        ("GET", "/cases/CASE-missing", {}),
        ("GET", "/cases/CASE-missing/history", {}),
        ("PATCH", "/cases/CASE-missing/status", {"json": {"new_status": "OPEN"}}),
    ],
)
def test_missing_case_returns_not_found(client, method, path, options):
    response = client.request(method, path, **options)
    assert response.status_code == 404
    assert response.json() == {"detail": "Case not found"}


@pytest.mark.parametrize(
    ("payload", "expected_status"),
    [
        ({"new_status": "CLOSED"}, 409),
        ({"new_status": "UNKNOWN"}, 422),
        ({}, 422),
        ({"new_status": "OPEN", "reason": 123}, 422),
    ],
)
def test_rejected_status_change_preserves_case_and_history(client, payload, expected_status):
    response = client.post("/cases", json={"title": "Sample delivery"})
    assert response.status_code == 201
    path = f"/cases/{response.json()['case_id']}"
    case_before = client.get(path).json()
    history_before = client.get(f"{path}/history").json()

    response = client.patch(f"{path}/status", json=payload)
    assert response.status_code == expected_status
    assert client.get(path).json() == case_before
    assert client.get(f"{path}/history").json() == history_before

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict

from main import ALLOWED_TRANSITIONS, create_case, transition_case
from storage import init_db, load_cases, save_case, save_status_change

@asynccontextmanager
async def lifespan(_app: FastAPI):
    init_db()
    yield

app = FastAPI(title="FlowDesk API", lifespan=lifespan)

@app.get("/cases")
def list_cases():
    cases = []
    for case in load_cases().values():
        cases.append({
            "case_id": case["case_id"],
            "title": case["title"],
            "status": case["status"],
        })
    return cases

@app.get("/cases/{case_id}")
def get_case(case_id: str):
    case = load_cases().get(case_id)
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    return {
        "case_id": case["case_id"],
        "title": case["title"],
        "description": case["description"],
        "status": case["status"],
        "created_at": case["created_at"],
        "updated_at": case["updated_at"],
    }


@app.get("/cases/{case_id}/history")
def get_case_history(case_id: str):
    case = load_cases().get(case_id)
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    return case["history"]
class CaseCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    description: str = ""

@app.post("/cases", status_code=201)
def create_case_endpoint(body: CaseCreate):
    try:
        case = create_case(body.title, body.description)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error

    save_case(case)
    return {field: value for field, value in case.items() if field != "history"}

class CaseStatusUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    new_status: str
    reason: str | None = None


@app.patch("/cases/{case_id}/status")
def update_case_status(case_id: str, body: CaseStatusUpdate):
    case = load_cases().get(case_id)
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")

    current_status = case["status"]
    new_status = body.new_status.strip().upper()
    if new_status not in ALLOWED_TRANSITIONS:
        raise HTTPException(status_code=422, detail="Unknown status")

    reason = (body.reason or "").strip() or None
    if not transition_case(case, new_status, reason):
        raise HTTPException(
            status_code=409,
            detail=f"Cannot move from {current_status} to {new_status}",
        )

    save_status_change(case)
    return {
        "case_id": case_id,
        "status": case["status"],
        "updated_at": case["updated_at"],
    }
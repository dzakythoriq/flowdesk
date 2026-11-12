from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from storage import init_db, load_cases

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
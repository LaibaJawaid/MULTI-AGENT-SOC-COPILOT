from fastapi import APIRouter

from app.schemas.investigation import InvestigationRequest

from app.agents.supervisor_agent import investigate

router = APIRouter(tags=["Investigation"])


@router.post("/investigate")

def run_investigation(data: InvestigationRequest):

    return investigate(data)
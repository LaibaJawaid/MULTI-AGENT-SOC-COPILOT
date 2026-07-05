from fastapi import APIRouter

from app.agents.threat_intel_agent import analyze_threat

router = APIRouter(

    prefix="/threat",

    tags=["Threat Intelligence"]

)


@router.post("/")
def threat_lookup(alert: dict):

    """
    Analyze threat intelligence
    for an incoming alert.
    """

    return analyze_threat(alert)
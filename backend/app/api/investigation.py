from fastapi import APIRouter

from app.agents.explainer_agent import explain

router = APIRouter(
    prefix="/explain",
    tags=["Explainability"]
)


@router.post("/")
def explain_alert(alert: dict):

    return explain(alert)
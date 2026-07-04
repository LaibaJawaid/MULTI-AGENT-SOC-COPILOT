from fastapi import APIRouter

from app.agents.recommendation_agent import recommend

router = APIRouter(
    prefix="/recommend",
    tags=["Recommendation"]
)


@router.post("/")
def get_recommendation(alert: dict):

    return recommend(alert)
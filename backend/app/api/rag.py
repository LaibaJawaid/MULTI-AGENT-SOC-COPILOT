from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.postgres import get_db

from app.models.alert import Alert

from app.agents.rag_agent import rag_agent

router = APIRouter(tags=["RAG"])


@router.post("/rag/{alert_id}")

def rag(alert_id: int, db: Session = Depends(get_db)):

    alert = db.query(Alert).filter(Alert.id == alert_id).first()

    if not alert:

        return {

            "message": "Alert not found"

        }

    rag_agent.store(alert)

    results = rag_agent.retrieve(alert)

    return results
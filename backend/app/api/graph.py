from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from app.db.postgres import get_db

from app.models.alert import Alert

from app.agents.graph_agents import graph_agent

router=APIRouter(tags=["Graph"])


@router.post("/graph/{alert_id}")

def build_graph(

    alert_id:int,

    db:Session=Depends(get_db)

):

    alert=db.query(Alert).filter(

        Alert.id==alert_id

    ).first()

    if not alert:

        return{

            "message":"Alert not found"

        }

    graph_agent.build(alert)

    return{

        "message":"Graph Created"

    }


@router.get("/graph/{alert_id}")

def get_graph(alert_id:int):

    return graph_agent.investigate(alert_id)
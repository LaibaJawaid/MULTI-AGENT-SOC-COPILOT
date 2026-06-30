from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.postgres import get_db
from app.schemas.alert import AlertCreate
from app.crud.alerts import create_alert, get_alerts

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)


@router.post("/")
def add_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db)
):

    return create_alert(db, alert)


@router.get("/")
def read_alerts(
    db: Session = Depends(get_db)
):

    return get_alerts(db)
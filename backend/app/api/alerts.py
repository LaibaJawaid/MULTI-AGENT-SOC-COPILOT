from fastapi import APIRouter

from fastapi import Depends

from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.postgres import get_db

from app.schemas.alert import AlertCreate

from app.crud.alerts import create_alert, get_alerts


router = APIRouter(tags=["Alerts"])


@router.post("/alerts")

def create(alert: AlertCreate,
           db: Session = Depends(get_db)):

    result = create_alert(db, alert)

    if result is None:

        raise HTTPException(

            status_code=400,

            detail="Duplicate Alert"

        )

    return result


@router.get("/alerts")

def read(db: Session = Depends(get_db)):

    return get_alerts(db)
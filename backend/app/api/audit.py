"""
Audit API

Allows manager to see
everything AI has done.
"""

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.postgres import get_db

from app.crud.audit import get_logs

router = APIRouter(

    prefix="/audit",

    tags=["Audit"]

)


@router.get("/")

def history(

    db: Session = Depends(get_db)

):
    return get_logs(db)
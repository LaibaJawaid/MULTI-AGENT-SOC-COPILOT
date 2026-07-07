"""
Case Notes API
"""

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.postgres import get_db

from app.schemas.case_note import (
    CaseNoteCreate,
    CaseNoteResponse
)

from app.crud.case_notes import (
    add_note,
    get_notes
)

router = APIRouter(

    prefix="/case-notes",

    tags=["Case Notes"]

)


# -------------------------------------
# Add Analyst Note
# -------------------------------------
@router.post(

    "/",

    response_model=CaseNoteResponse

)

def create_case_note(

    note: CaseNoteCreate,

    db: Session = Depends(get_db)

):

    return add_note(db, note)


# -------------------------------------
# Get Notes of Alert
# -------------------------------------
@router.get("/{alert_id}")

def read_notes(

    alert_id: int,

    db: Session = Depends(get_db)

):

    return get_notes(db, alert_id)
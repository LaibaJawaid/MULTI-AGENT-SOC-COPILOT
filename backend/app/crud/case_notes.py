"""
CRUD for Case Notes
"""

from sqlalchemy.orm import Session

from app.models.case_note import CaseNote


# -------------------------------------
# Add Note
# -------------------------------------
def add_note(db: Session, note):

    db_note = CaseNote(

        alert_id=note.alert_id,

        analyst=note.analyst,

        note=note.note

    )

    db.add(db_note)

    db.commit()

    db.refresh(db_note)

    return db_note


# -------------------------------------
# Get Notes
# -------------------------------------
def get_notes(db: Session, alert_id: int):

    return (

        db.query(CaseNote)

        .filter(CaseNote.alert_id == alert_id)

        .all()

    )
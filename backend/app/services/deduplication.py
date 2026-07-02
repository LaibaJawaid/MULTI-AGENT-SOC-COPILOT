from sqlalchemy.orm import Session

from app.models.alert import Alert


def is_duplicate(db: Session, title: str):

    alert = (
        db.query(Alert)
        .filter(Alert.title == title)
        .first()
    )

    return alert is not None
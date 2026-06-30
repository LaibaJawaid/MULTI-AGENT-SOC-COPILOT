from sqlalchemy.orm import Session
from app.models.alert import Alert
from app.schemas.alert import AlertCreate


def create_alert(db: Session, alert: AlertCreate):

    db_alert = Alert(
        severity=alert.severity,
        source=alert.source,
        ip=alert.ip,
        description=alert.description,
    )

    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)

    return db_alert


def get_alerts(db: Session):

    return db.query(Alert).all()
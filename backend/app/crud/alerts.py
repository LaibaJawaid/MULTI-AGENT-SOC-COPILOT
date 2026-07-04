from sqlalchemy.orm import Session

from app.models.alert import Alert

from app.agents.soc_agent import analyze_alert

from app.services.vector_store import store_alert

from app.services.graph import save_alert_graph


def create_alert(db, alert):

    ai = analyze_alert(db, alert)

    if ai["duplicate"]:

        return None

    db_alert = Alert(

        title=alert.title,

        description=alert.description,

        severity=ai["severity"],

        category=ai["category"],

        summary=ai["summary"],

        recommendation="\n".join(ai["actions"]),

        status="OPEN"

    )

    db.add(db_alert)

    db.commit()

    db.refresh(db_alert)

    store_alert(db_alert)

    save_alert_graph(db_alert)

    return db_alert


def get_alerts(db: Session):

    return db.query(Alert).all()
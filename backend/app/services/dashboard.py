"""
Dashboard Analytics Service

Provides statistics for SOC Dashboard.
"""

from sqlalchemy.orm import Session

from app.models.alert import Alert


def dashboard_stats(db: Session):

    total = db.query(Alert).count()

    open_alerts = db.query(Alert).filter(
        Alert.status == "OPEN"
    ).count()

    closed = db.query(Alert).filter(
        Alert.status == "CLOSED"
    ).count()

    critical = db.query(Alert).filter(
        Alert.severity == "CRITICAL"
    ).count()

    high = db.query(Alert).filter(
        Alert.severity == "HIGH"
    ).count()

    medium = db.query(Alert).filter(
        Alert.severity == "MEDIUM"
    ).count()

    low = db.query(Alert).filter(
        Alert.severity == "LOW"
    ).count()

    return {

        "total_alerts": total,

        "open_alerts": open_alerts,

        "closed_alerts": closed,

        "critical": critical,

        "high": high,

        "medium": medium,

        "low": low
    }
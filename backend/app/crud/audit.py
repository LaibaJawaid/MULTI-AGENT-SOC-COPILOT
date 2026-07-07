"""
Database operations for Audit Logs.
"""

from sqlalchemy.orm import Session

from app.models.audit import AuditLog


def create_log(db, log):

    entry = AuditLog(

        agent=log.agent,

        action=log.action,

        details=log.details

    )

    db.add(entry)

    db.commit()

    db.refresh(entry)

    return entry


def get_logs(db):

    return db.query(AuditLog).order_by(
        AuditLog.timestamp.desc()
    ).all()
"""
Reusable logger.

Every AI Agent can call this.
"""

from app.schemas.audit import AuditCreate

from app.crud.audit import create_log


def log_event(

    db,

    agent,

    action,

    details

):
    log = AuditCreate(

        agent=agent,

        action=action,

        details=details

    )

    return create_log(db, log)
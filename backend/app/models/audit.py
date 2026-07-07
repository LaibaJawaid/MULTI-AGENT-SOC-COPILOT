"""
Audit Model

Stores every investigation event.

Useful for:

✔ compliance
✔ SOC timeline
✔ reporting
"""

from sqlalchemy import Column, Integer, String, Text, DateTime

from datetime import datetime

from app.db.base import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)

    agent = Column(String)

    action = Column(String)

    details = Column(Text)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )
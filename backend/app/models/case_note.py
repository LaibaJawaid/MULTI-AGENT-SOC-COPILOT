"""
Case Notes Model

Stores analyst notes
for every investigation.

Example:
---------
Alert #15

Analyst:
PowerShell attack confirmed.

Host isolated.

Waiting for memory dump.
"""

from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base


class CaseNote(Base):

    __tablename__ = "case_notes"

    id = Column(Integer, primary_key=True, index=True)

    alert_id = Column(Integer)

    analyst = Column(String(100))

    note = Column(Text)
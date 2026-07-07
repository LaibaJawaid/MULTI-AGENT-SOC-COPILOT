"""
Pydantic schemas for Audit Logs.
"""

from pydantic import BaseModel
from datetime import datetime


class AuditCreate(BaseModel):

    agent: str

    action: str

    details: str


class AuditResponse(AuditCreate):

    id: int

    timestamp: datetime

    class Config:

        from_attributes = True
"""
Pydantic Schema
"""

from pydantic import BaseModel


class CaseNoteCreate(BaseModel):

    alert_id: int

    analyst: str

    note: str


class CaseNoteResponse(CaseNoteCreate):

    id: int

    class Config:

        from_attributes = True
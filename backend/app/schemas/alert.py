from pydantic import BaseModel
from datetime import datetime


class AlertCreate(BaseModel):
    severity: str
    source: str
    ip: str
    description: str


class AlertResponse(AlertCreate):
    id: int
    created_at: datetime
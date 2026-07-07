"""
Dashboard Response Schema
"""

from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_alerts: int
    open_alerts: int
    closed_alerts: int
    critical: int
    high: int
    medium: int
    low: int
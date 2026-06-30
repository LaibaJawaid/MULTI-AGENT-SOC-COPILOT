from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.db.base import Base


class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    severity: Mapped[str] = mapped_column(String(20))

    source: Mapped[str] = mapped_column(String(100))

    ip: Mapped[str] = mapped_column(String(50))

    description: Mapped[str] = mapped_column(String(500))

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
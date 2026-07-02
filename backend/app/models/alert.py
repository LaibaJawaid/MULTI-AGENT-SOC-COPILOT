from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.base import Base


class Alert(Base):

    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    description = Column(String)

    severity = Column(String)

    category = Column(String)

    summary = Column(String)

    recommendation = Column(String)

    status = Column(String)
"""
Database Models
"""
from datetime import datetime
from zoneinfo import ZoneInfo
from datetime import datetime
from sqlalchemy import Date


from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Enum,
    Integer,
    String,
)

from app.database.base import Base
from app.schemas.task import Priority


class Task(Base):
    """
    Task Database Model
    """

    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    title = Column(
        String(255),
        nullable=False,
    )

    due_date = Column(
        Date,
        nullable=True,
    )

    priority = Column(
        Enum(Priority),
        nullable=False,
        default=Priority.MEDIUM,
    )

    created_at = Column(
    DateTime(timezone=True),
    default=lambda: datetime.now(
        ZoneInfo("Asia/Kolkata")
    ),
    nullable=False,
)

    def __repr__(self):

        return (
            f"<Task(id={self.id}, "
            f"title='{self.title}', "
            f"priority='{self.priority.value}')>"
        )
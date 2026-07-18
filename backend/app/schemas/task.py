"""
Task Schemas
"""

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TaskBase(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=255,
        description="Task title"
    )

    due_date: date | None = Field(
        default=None,
        description="Task due date"
    )

    priority: Priority = Field(
        default=Priority.MEDIUM
    )


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
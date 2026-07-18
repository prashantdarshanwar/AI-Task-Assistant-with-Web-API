"""
Task Service

Contains task-related business logic.
"""

from sqlalchemy.orm import Session

from app.crud.task_crud import (
    get_all_tasks,
    get_task_by_id,
)


def list_tasks(db: Session):
    return get_all_tasks(db)


def get_task(db: Session, task_id: int):
    return get_task_by_id(db, task_id)
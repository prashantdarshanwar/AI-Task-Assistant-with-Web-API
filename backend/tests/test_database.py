"""
Database Tests
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))



from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.database.models import Task
from app.schemas.task import Priority

from datetime import date


def test_database_connection():

    db = SessionLocal()

    assert isinstance(db, Session)

    db.close()


def test_create_task():

    db = SessionLocal()

    task = Task(
        title="Database Test",
        due_date=date.today(),
        priority=Priority.MEDIUM,
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    assert task.id is not None

    db.delete(task)

    db.commit()

    db.close()


def test_read_tasks():

    db = SessionLocal()

    tasks = db.query(Task).all()

    assert isinstance(tasks, list)

    db.close()
from sqlalchemy.orm import Session

from app.database.models import Task
from app.schemas.task import TaskCreate


class TaskCRUD:

    @staticmethod
    def create_task(
        db: Session,
        task: TaskCreate,
    ) -> Task:

        db_task = Task(
            title=task.title,
            due_date=task.due_date,
            priority=task.priority,
        )

        db.add(db_task)
        db.commit()
        db.refresh(db_task)

        return db_task

    @staticmethod
    def get_all_tasks(
        db: Session,
    ):

        return (
            db.query(Task)
            .order_by(Task.created_at.desc())
            .all()
        )

    @staticmethod
    def get_task_by_id(
        db: Session,
        task_id: int,
    ):

        return (
            db.query(Task)
            .filter(Task.id == task_id)
            .first()
        )
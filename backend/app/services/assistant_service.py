"""
Assistant Service

Business logic for AI Task Assistant.
"""

import logging

from sqlalchemy.orm import Session

from app.crud.task_crud import TaskCRUD
from app.llm.parser import parse_task
from app.schemas.task import TaskResponse


logger = logging.getLogger(__name__)


class AssistantService:
    """
    Handles AI task creation workflow.
    """

    @staticmethod
    def create_task_from_query(
        db: Session,
        query: str,
    ) -> TaskResponse:
        """
        Complete workflow:

        User Query
            ↓
        LLM
            ↓
        Validator
            ↓
        Date Parser
            ↓
        Database
            ↓
        Response
        """

        logger.info("Received query: %s", query)

        # -----------------------------
        # Parse using LLM
        # -----------------------------
        task_data = parse_task(query)

        logger.info(
            "LLM Parsed Task: %s",
            task_data.model_dump()
        )

        # -----------------------------
        # Save Task
        # -----------------------------
        task = TaskCRUD.create_task(
            db=db,
            task=task_data,
        )

        logger.info(
            "Task saved successfully (ID=%s)",
            task.id,
        )

        # -----------------------------
        # Return Response
        # -----------------------------
        return TaskResponse.model_validate(task)

    @staticmethod
    def list_tasks(
        db: Session,
    ) -> list[TaskResponse]:

        tasks = TaskCRUD.get_all_tasks(db)

        return [
            TaskResponse.model_validate(task)
            for task in tasks
        ]

    @staticmethod
    def get_task(
        db: Session,
        task_id: int,
    ) -> TaskResponse | None:

        task = TaskCRUD.get_task_by_id(
            db,
            task_id,
        )

        if task is None:
            return None

        return TaskResponse.model_validate(task)
"""
LLM Output Validator
"""

from pydantic import ValidationError

from app.schemas.task import Priority, TaskCreate
from app.services.date_service import parse_due_date


VALID_PRIORITIES = {
    "low": Priority.LOW,
    "medium": Priority.MEDIUM,
    "high": Priority.HIGH,
}


def validate_task(data: dict) -> TaskCreate:
    """
    Validate and normalize LLM output.
    """

    try:

        # -----------------------------------
        # Keep only expected fields
        # -----------------------------------
        allowed_fields = {
            "title",
            "due_date",
            "priority",
        }

        data = {
            key: value
            for key, value in data.items()
            if key in allowed_fields
        }

        # -----------------------------------
        # Title
        # -----------------------------------
        title = str(
            data.get("title", "")
        ).strip()

        if not title:
            raise ValueError(
                "Task title is required."
            )

        data["title"] = title

        # -----------------------------------
        # Priority
        # -----------------------------------
        priority = str(
            data.get("priority", "medium")
        ).strip().lower()

        data["priority"] = VALID_PRIORITIES.get(
            priority,
            Priority.MEDIUM,
        )

        # -----------------------------------
        # Due Date
        # -----------------------------------
        raw_due_date = data.get("due_date")

        if raw_due_date in (
            None,
            "",
            "null",
            "None",
            "N/A",
            "na",
            "no due date",
        ):
            data["due_date"] = None

        else:

            parsed_due_date = parse_due_date(
                raw_due_date
            )

            if parsed_due_date is None:

                raise ValueError(
                    f"Unable to parse due date: '{raw_due_date}'"
                )

            data["due_date"] = parsed_due_date

        # -----------------------------------
        # Validate using Pydantic
        # -----------------------------------
        task = TaskCreate.model_validate(data)

        return task

    except ValidationError as e:

        raise ValueError(
            f"Pydantic Validation Error:\n{e}"
        )

    except Exception as e:

        raise ValueError(str(e))
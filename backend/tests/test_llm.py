"""
LLM Parser Tests
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))



from app.llm.validator import validate_task
from app.services.date_service import parse_due_date
from app.schemas.task import Priority


def test_validate_task():

    data = {
        "title": "Fix Login Bug",
        "priority": "high",
        "due_date": "tomorrow",
    }

    task = validate_task(data)

    assert task.title == "Fix Login Bug"

    assert task.priority == Priority.HIGH

    assert task.due_date is not None


def test_default_priority():

    data = {
        "title": "Update README",
        "due_date": "Friday",
    }

    task = validate_task(data)

    assert task.priority == Priority.MEDIUM


def test_parse_today():

    assert parse_due_date("today") is not None


def test_parse_tomorrow():

    assert parse_due_date("tomorrow") is not None


def test_parse_next_friday():

    assert parse_due_date("next Friday") is not None


def test_parse_next_month_saturday():

    assert parse_due_date("next month Saturday") is not None


def test_parse_custom_date():

    assert parse_due_date("25 July") is not None


def test_parse_iso_date():

    assert parse_due_date("2026-07-25") is not None


def test_invalid_title():

    try:

        validate_task(
            {
                "title": "",
                "priority": "high",
            }
        )

        assert False

    except ValueError:

        assert True


def test_invalid_priority():

    data = {
        "title": "Fix Bug",
        "priority": "unknown",
    }

    task = validate_task(data)

    assert task.priority == Priority.MEDIUM
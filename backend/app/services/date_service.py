"""
Date Service

Converts natural language dates into Python date objects.
"""

from datetime import date, datetime, timedelta
from calendar import monthrange
from typing import Optional
import re

import dateparser


WEEKDAYS = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}


class DateService:

    @staticmethod
    def _first_weekday(year: int, month: int, weekday: int) -> date:
        current = datetime(year, month, 1)

        while current.weekday() != weekday:
            current += timedelta(days=1)

        return current.date()

    @staticmethod
    def _next_weekday(weekday: int) -> date:
        today = datetime.now()

        days = (weekday - today.weekday() + 7) % 7

        if days == 0:
            days = 7

        return (today + timedelta(days=days)).date()

    @staticmethod
    def _this_weekday(weekday: int) -> date:
        today = datetime.now()

        days = weekday - today.weekday()

        if days < 0:
            days += 7

        return (today + timedelta(days=days)).date()

    @staticmethod
    def _handle_custom_cases(text: str) -> Optional[date]:

        text = text.lower().strip()

        now = datetime.now()

        # -------------------------
        # Today / Tomorrow
        # -------------------------

        if text == "today":
            return now.date()

        if text == "tomorrow":
            return (now + timedelta(days=1)).date()

        if text == "day after tomorrow":
            return (now + timedelta(days=2)).date()

        if text == "yesterday":
            return (now - timedelta(days=1)).date()

        # -------------------------
        # Next Week
        # -------------------------

        if text == "next week":
            return (now + timedelta(days=7)).date()

        # -------------------------
        # Next Month
        # -------------------------

        if text == "next month":

            if now.month == 12:
                return date(now.year + 1, 1, 1)

            return date(now.year, now.month + 1, 1)

        # -------------------------
        # End Of This Month
        # -------------------------

        if text == "end of this month":

            last = monthrange(now.year, now.month)[1]

            return date(now.year, now.month, last)

        # -------------------------
        # Beginning Of Next Month
        # -------------------------

        if text in {
            "beginning of next month",
            "start of next month",
        }:

            if now.month == 12:
                return date(now.year + 1, 1, 1)

            return date(now.year, now.month + 1, 1)

        # -------------------------
        # Next Friday
        # -------------------------

        match = re.fullmatch(
            r"next (monday|tuesday|wednesday|thursday|friday|saturday|sunday)",
            text,
        )

        if match:

            return DateService._next_weekday(
                WEEKDAYS[match.group(1)]
            )

        # -------------------------
        # This Friday
        # -------------------------

        match = re.fullmatch(
            r"this (monday|tuesday|wednesday|thursday|friday|saturday|sunday)",
            text,
        )

        if match:

            return DateService._this_weekday(
                WEEKDAYS[match.group(1)]
            )

        # -------------------------
        # Next Month Friday
        # -------------------------

        match = re.fullmatch(
            r"next month (monday|tuesday|wednesday|thursday|friday|saturday|sunday)",
            text,
        )

        if match:

            weekday = WEEKDAYS[match.group(1)]

            if now.month == 12:
                year = now.year + 1
                month = 1
            else:
                year = now.year
                month = now.month + 1

            return DateService._first_weekday(
                year,
                month,
                weekday,
            )

        return None

    @staticmethod
    def parse_due_date(
        date_text: Optional[str],
    ) -> Optional[date]:

        if not date_text:
            return None

        date_text = str(date_text).strip()

        if date_text.lower() in {
            "",
            "null",
            "none",
            "n/a",
            "na",
            "no due date",
        }:
            return None

        # ISO Date

        try:

            return datetime.strptime(
                date_text,
                "%Y-%m-%d",
            ).date()

        except ValueError:
            pass

        # Custom Cases

        custom = DateService._handle_custom_cases(
            date_text,
        )

        if custom:
            return custom

        # dateparser Fallback

        parsed = dateparser.parse(
            date_text,
            settings={
                "RELATIVE_BASE": datetime.now(),
                "PREFER_DATES_FROM": "future",
                "DATE_ORDER": "DMY",
                "STRICT_PARSING": False,
            },
        )

        if parsed:
            return parsed.date()

        return None


def parse_due_date(
    text: Optional[str],
) -> Optional[date]:

    return DateService.parse_due_date(text)
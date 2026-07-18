"""
LLM Parser
"""

import json

from app.core.config import settings
from app.core.prompt import SYSTEM_PROMPT
from app.llm.client import client
from app.llm.validator import validate_task


def parse_task(query: str):

    response = client.chat.completions.create(

        model=settings.MODEL,

        temperature=0,

        response_format={
            "type": "json_object"
        },

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": query,
            },
        ],
    )

    content = response.choices[0].message.content

    print("\n===== RAW LLM OUTPUT =====")
    print(content)

    data = json.loads(content)

    print("\n===== BEFORE VALIDATION =====")
    print(data)

    validated = validate_task(data)

    print("\n===== AFTER VALIDATION =====")
    print(validated.model_dump())

    return validated
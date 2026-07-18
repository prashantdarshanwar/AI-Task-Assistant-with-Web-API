from pydantic import BaseModel, Field


class AssistantRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Natural language task request"
    )
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.assistant import AssistantRequest
from app.schemas.task import TaskResponse
from app.services.assistant_service import AssistantService

router = APIRouter(
    prefix="",
    tags=["Assistant"],
)


@router.post(
    "/assistant",
    response_model=TaskResponse,
)
def assistant(
    request: AssistantRequest,
    db: Session = Depends(get_db),
):

    return AssistantService.create_task_from_query(
        db=db,
        query=request.query,
    )
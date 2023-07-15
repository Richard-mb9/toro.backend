from fastapi import APIRouter
from http import HTTPStatus

from src.services import SPBService
from src.services.schemas import SPBEventRequest

router = APIRouter()


@router.post("/events", status_code=HTTPStatus.OK)
async def events(event: SPBEventRequest):
    return SPBService().execute_event(event)

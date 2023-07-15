from pydantic import BaseModel, model_validator
from src.commons.errors import BadRequestError


class SPBEventTargetRequest(BaseModel):
    """Model target for event from spb"""

    bank: str
    branch: str
    account: str


class SPBEventOriginRequest(BaseModel):
    """Model origin for event from spb"""

    bank: str
    branch: str
    cpf: str


class SPBEventRequest(BaseModel):
    """Model events for event from spb"""

    event: str
    target: SPBEventTargetRequest
    origin: SPBEventOriginRequest
    amount: float

    @model_validator(mode="after")
    def validate_event(self):
        event = self.event
        if event != "TRANSFER":
            raise BadRequestError("Invalid event")

        return self

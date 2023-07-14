import re
from pydantic import BaseModel
from pydantic import model_validator
from src.commons.errors import BadRequestError


class UpdateUserRequest(BaseModel):
    """Model Update User"""

    email: str = None
    name: str = None
    cpf: str = None

    @model_validator(mode="after")
    def validate_email(self):
        email = self.email
        regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$"
        if email is not None and not re.fullmatch(regex, email):
            raise BadRequestError("Invalid email")
        return self

    @model_validator(mode="after")
    def validate_cpf(self):
        cpf = self.cpf
        if cpf is not None:
            try:
                int(cpf)
            except ValueError:
                raise BadRequestError("Invalid CPF")

            if len(cpf) < 11:
                raise BadRequestError("Invalid CPF")

        return self

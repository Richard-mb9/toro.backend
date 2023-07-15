import re
from pydantic import BaseModel
from pydantic import Field, model_validator
from src.commons.errors import BadRequestError


class CreateUserRequest(BaseModel):
    """Model Create User"""

    email: str
    password: str = Field(
        description="min 8 digits and max 24 digits", example="123456"
    )
    name: str
    cpf: str

    @model_validator(mode="after")
    def validate_password(self):
        password = self.password
        if len(password) < 8:
            raise BadRequestError("password must contain at least 8 digits")
        if len(password) > 24:
            raise BadRequestError(
                "The password must contain a maximum of 24 characters"
            )

        return self

    @model_validator(mode="after")
    def validate_email(self):
        email = self.email
        regex = "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        if not re.fullmatch(regex, email):
            raise BadRequestError("Invalid email")
        return self

    @model_validator(mode="after")
    def validate_cpf(self):
        cpf = self.cpf
        try:
            int(cpf)
        except ValueError:
            raise BadRequestError("Invalid CPF")

        if len(cpf) < 11:
            raise BadRequestError("Invalid CPF")

        return self

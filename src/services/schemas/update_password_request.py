from pydantic import BaseModel
from src.commons.errors import BadRequestError
from pydantic import Field, model_validator


class UpdatePasswordRequest(BaseModel):
    """Model for Update password from user"""

    current_password: str = Field(description="current password")
    new_password: str = Field(
        description="min 8 digits and max 24 digits", example="123456"
    )

    @model_validator(mode="after")
    def validate_password(self):
        new_password = self.new_password
        current_password = self.current_password

        if current_password == new_password:
            raise BadRequestError(
                "the new password cannot be the same as the current password"
            )
        if len(new_password) < 8:
            raise BadRequestError("password must contain at least 8 digits")
        if len(new_password) > 24:
            raise BadRequestError(
                "The password must contain a maximum of 24 characters"
            )

        return self

from pydantic import BaseModel


class AuthRequest(BaseModel):
    """Model for Authenticate User"""

    email: str
    password: str

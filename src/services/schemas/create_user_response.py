from dataclasses import dataclass


@dataclass
class CreateUserResponse:
    """Response from request create user"""

    id: int

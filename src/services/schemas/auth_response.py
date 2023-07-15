from dataclasses import dataclass


@dataclass
class AuthResponse:
    """Response from Request Auth"""

    access_token: str
    token_type: str

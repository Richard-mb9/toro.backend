from dataclasses import dataclass


@dataclass
class GetAccountDataResponse:
    """Type Account Data Response"""

    account: str
    branch: str

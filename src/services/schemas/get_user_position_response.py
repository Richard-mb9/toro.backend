from dataclasses import dataclass
from typing import List
from decimal import Decimal


@dataclass
class AssetsFromUserPositionResponse:
    """Type Assets from user position Response"""

    code: str
    quantity: int
    current_price: Decimal
    name: str


@dataclass
class GetUserPositionResponse:
    """Type User Position Response"""

    checking_account_amount: Decimal
    positions: List[AssetsFromUserPositionResponse]
    consolidated: Decimal

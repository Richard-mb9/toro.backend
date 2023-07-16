from dataclasses import dataclass
from typing import List
from decimal import Decimal


@dataclass
class AssetsFromUserPositionResponse:
    """Type Assets from user position Response"""

    code: str
    quantity: str
    current_price: str


@dataclass
class GetUserPositionResponse:
    """Type User Position Response"""

    checking_account_amount: Decimal
    positions: List[AssetsFromUserPositionResponse]
    consolidated: Decimal

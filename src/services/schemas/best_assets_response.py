from dataclasses import dataclass
from decimal import Decimal


@dataclass
class BestAssetResponse:
    """Type Best Asset"""

    symbol: str
    sold: int
    current_price: Decimal

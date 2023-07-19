from dataclasses import dataclass


@dataclass
class AssetResponse:
    """Type Asset Response"""

    symbol: str
    name: str
    current_price: float

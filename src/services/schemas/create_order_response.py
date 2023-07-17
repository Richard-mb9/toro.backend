from dataclasses import dataclass


@dataclass
class CreateOrderResponse:
    """Type Response for endpoint create order"""

    order: int

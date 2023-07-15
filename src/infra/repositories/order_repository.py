from src.domain import Order
from .base_repository import BaseRepository


class OrderRepository(BaseRepository):
    """Repository from Orders"""

    def __init__(self):
        super().__init__(Order)

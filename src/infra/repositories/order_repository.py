from typing import TypedDict, List
from decimal import Decimal
from sqlalchemy.sql import text
from src.domain import Order
from .base_repository import BaseRepository


class ResultBestSellingAssets(TypedDict):
    """Type Best Assets"""

    symbol: str
    sold: int
    current_price: Decimal


class OrderRepository(BaseRepository):
    """Repository from Orders"""

    def __init__(self):
        super().__init__(Order)

    def filter_by_last_days(
        self, interval: int, limit: int
    ) -> List[ResultBestSellingAssets]:
        query = (
            "select \n"
            "o.asset_code as symbol, \n"
            "SUM(o.quantity)  as sold,, \n"
            "a.price as current_price \n"
            "from orders o \n"
            "inner join assets a on a.code  = o.asset_code \n"
            f"where o.created_at > DATE_SUB(CURRENT_TIMESTAMP, INTERVAL {interval} DAY) \n"
            "GROUP BY asset_code \n"
            "order by sold DESC \n"
            f"LIMIT {limit};"
        )

        result = self.session.execute((text(query)))

        return super().format_search_query(result)

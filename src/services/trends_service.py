from src.services import OrderService


class TrendsService:
    """Trends Service"""

    def filter_best_assets_by_last_days(self, interval: int, limit: int):
        return OrderService().filter_by_last_days(interval, limit)

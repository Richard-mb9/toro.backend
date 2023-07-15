from src.domain import Asset
from .base_repository import BaseRepository


class AssetsRepository(BaseRepository):
    """Repository for Assets"""

    def __init__(self):
        super().__init__(Asset)

    def find_by_code(self, code: str) -> Asset | None:
        return self.session.query(self.entity).filter_by(code=code).first()

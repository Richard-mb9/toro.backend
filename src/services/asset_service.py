from src.infra.repositories import AssetsRepository


class AssetService:
    """Service for use Assets"""

    def __init__(self):
        self.repository = AssetsRepository()

    def find_by_code(self, code: str):
        return self.repository.find_by_code(code)

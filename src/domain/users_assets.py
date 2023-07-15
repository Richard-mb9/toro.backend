from sqlalchemy import Column, Integer, String, ForeignKey

from src.config import Base


class UsersAssets(Base):
    """Assets from Users Entity"""

    __tablename__ = "users_assets"

    user_id = user_id = Column(
        Integer, ForeignKey("users.id"), primary_key=True, nullable=False
    )
    asset_code = Column(
        String(10), ForeignKey("assets.code"), primary_key=True, nullable=False
    )
    quantity = Column(Integer, nullable=False)

    def __repr__(self):  # pragma: no cover
        return f"User {self.user_id}, asset {self.asset_code}"

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from src.config import Base


class Order(Base):
    """Order Entity"""

    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    asset_code = Column(String(10), ForeignKey("assets.code"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unity_value = Column(DECIMAL(10, 2), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):  # pragma: no cover
        return f"User {self.user_id}, asset {self.asset_code}"

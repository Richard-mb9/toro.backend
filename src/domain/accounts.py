from sqlalchemy import Column, DECIMAL, String, Integer, ForeignKey
from src.config import Base


class Account(Base):
    """Accounts Entity"""

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    branch = Column(
        String(5),
        server_default="0001",
    )
    amount = Column(DECIMAL(10, 2), server_default="0")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

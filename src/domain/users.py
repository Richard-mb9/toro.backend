from sqlalchemy import Column, Integer, String, ForeignKey, Table
from src.config import Base
from sqlalchemy.orm import relationship

user_assets = Table(
    "user_assets",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("assets_code", String(10), ForeignKey("assets.code")),
    Column("quantity", Integer, server_default="0"),
)


class User(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    cpf = Column(String(20), nullable=False, unique=True)
    assets = relationship("Asset", secondary=user_assets)

    def __repr__(self):  # pragma: no cover
        return f"User {self.email}"

from src.config import Base

from sqlalchemy import Column, DECIMAL, String


class Asset(Base):
    """Assets Entity"""

    __tablename__ = "assets"

    code = Column(String(10), primary_key=True, unique=True)
    name = Column(String(100), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    def __repr__(self):  # pragma: no cover
        return f"asset {self.name}"

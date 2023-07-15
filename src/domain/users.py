from sqlalchemy import Column, Integer, String
from src.config import Base


class User(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    cpf = Column(String(20), nullable=False, unique=True)

    def __repr__(self):  # pragma: no cover
        return f"User {self.email}"

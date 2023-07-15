from pydantic import BaseModel


class OrderRequest(BaseModel):
    """Model Create order"""

    symbol: str
    amount: int

from pydantic import BaseModel
from datetime import datetime

# Transaction schema for request validation
class TransactionRequest(BaseModel):
    user_id: str
    source_currency: str
    source_amount: float
    target_currency: str

# Transaction schema for response validation
class TransactionResponse(TransactionRequest):
    id: int
    conversion_rate: float
    target_amount: float
    timestamp: datetime

    class Config:
        orm_mode = True
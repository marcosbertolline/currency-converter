from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.dependencies import Base

# Define the Transaction model
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    source_currency = Column(String)
    source_amount = Column(Float)
    target_currency = Column(String)
    conversion_rate = Column(Float)
    target_amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
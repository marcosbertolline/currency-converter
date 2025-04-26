from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction_schema import TransactionResponse
from app.dependencies import get_db

router = APIRouter()

# Endpoint to get all transactions for a user
@router.get("/transactions/{user_id}", response_model=list[TransactionResponse])
def get_transactions(user_id: str, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    return transactions

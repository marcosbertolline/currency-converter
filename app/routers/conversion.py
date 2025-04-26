from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction_schema import TransactionRequest, TransactionResponse
from app.services.currency_service import get_conversion_rate
from app.dependencies import get_db

router = APIRouter()

# Endpoint to convert EUR currency and store the transaction
@router.post("/convert", response_model=TransactionResponse)
def convert_currency(request: TransactionRequest, db: Session = Depends(get_db)):
    # Verify that at least one of the currencies is EUR
    if "EUR" not in [request.source_currency, request.target_currency]:
        raise HTTPException(
            status_code=400,
            detail="At least one of the currencies must be EUR."
        )

    try:
        rate = get_conversion_rate(request.source_currency, request.target_currency)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    target_amount = request.source_amount * rate
    
    transaction = Transaction(
        user_id=request.user_id,
        source_currency=request.source_currency,
        source_amount=request.source_amount,
        target_currency=request.target_currency,
        conversion_rate=rate,
        target_amount=target_amount
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction

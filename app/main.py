from fastapi import FastAPI
from app.dependencies import engine, Base
from app.routers import conversion, transactions

Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI()

# Include routers
app.include_router(conversion.router, prefix="/api")
app.include_router(transactions.router, prefix="/api")

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Currency Converter API running"}

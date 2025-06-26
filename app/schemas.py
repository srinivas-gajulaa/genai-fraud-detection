from pydantic import BaseModel

class TransactionInput(BaseModel):
    amount: float
    location_change: int
    velocity: float
    time_of_day: int

class PredictionResponse(BaseModel):
    fraud_score: float
    summary: str

from fastapi import FastAPI
from app.schemas import TransactionInput, PredictionResponse
from app.model import predict_fraud
from app.gpt_summary import generate_summary

app = FastAPI(title="GenAI Fraud Detection API")

@app.post("/predict", response_model=PredictionResponse)
def predict(txn: TransactionInput):
    txn_data = txn.dict()
    score = predict_fraud(txn_data)
    txn_data['score'] = score
    summary = generate_summary(txn_data)
    return PredictionResponse(fraud_score=score, summary=summary)

import joblib
import numpy as np

model = joblib.load("models/fraud_model.pkl")

def predict_fraud(features: dict) -> float:
    x = np.array([[features[k] for k in ['amount', 'location_change', 'velocity', 'time_of_day']]])
    return float(model.predict_proba(x)[0][1])

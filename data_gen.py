import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000
data = pd.DataFrame({
    'amount': np.random.exponential(500, n),
    'location_change': np.random.binomial(1, 0.1, n),
    'velocity': np.random.normal(10, 2, n),
    'time_of_day': np.random.randint(0, 24, n),
    'is_fraud': np.random.binomial(1, 0.1, n)
})
data.to_csv("data/transactions.csv", index=False)
print("✅ Data saved to data/transactions.csv")

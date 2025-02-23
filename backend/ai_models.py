import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Simulated dataset
data = {
    "budget_deviation": np.random.randint(-10, 50, 100),
    "worker_availability": np.random.randint(50, 100, 100),
    "equipment_status": np.random.randint(0, 2, 100),  # 0: Ok, 1: Needs maintenance
    "supply_chain_status": np.random.randint(0, 2, 100),
    "risk_label": np.random.choice(["Low", "Medium", "High"], 100),
}

df = pd.DataFrame(data)

# Train a simple model
X = df.drop(columns=["risk_label"])
y = df["risk_label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

def predict_risk():
    return model.predict([X_test.iloc[0].values])[0]

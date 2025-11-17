import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# small example: expects data/processed/flood_features.csv
DATA_PATH = "data/processed/flood_features.csv"
if not os.path.exists(DATA_PATH):
    print("No training data found at", DATA_PATH)
else:
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["date","flood_level"], errors="ignore")
    y = df["flood_level"]
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X, y)
    artifact = {"model": model, "version": "v1.0", "metrics": {}}
    os.makedirs("models", exist_ok=True)
    joblib.dump(artifact, "models/flood_rf_v1.joblib")
    print("Saved model to models/flood_rf_v1.joblib")

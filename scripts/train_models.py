import pandas as pd
import os
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

DATA_FILE = "data/processed/processed_metrics.csv"
MODEL_DIR = "models/saved_models"


def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def train():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Processed dataset not found: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)

    target = "load_avg_1"
    X = df.drop(columns=["timestamp", target])
    y = df[target]

    # Time-series split (no shuffle)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    models = {
        "linear_regression": LinearRegression(),
        "random_forest": RandomForestRegressor(
            n_estimators=200,
            max_depth=10,
            random_state=42
        ),
        "gradient_boosting": GradientBoostingRegressor(
            random_state=42
        )
    }

    ensure_dir(MODEL_DIR)

    results = []

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        rmse = np.sqrt(mean_squared_error(y_test, preds))
        results.append((name, rmse))

        joblib.dump(model, f"{MODEL_DIR}/{name}.pkl")
        print(f"[TRAINED] {name} RMSE = {rmse:.4f}")

    print("\n=== FINAL RMSE SUMMARY ===")
    for name, rmse in sorted(results, key=lambda x: x[1]):
        print(f"{name}: {rmse:.4f}")

    print(f"\n[SAVED] Models saved to {MODEL_DIR}")


if __name__ == "__main__":
    train()

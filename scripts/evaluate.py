import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error

DATA_FILE = "data/processed/processed_metrics.csv"
MODEL_DIR = "models/saved_models"
PLOTS_DIR = "results/plots"


def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def evaluate(model_name="random_forest"):
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Processed dataset not found: {DATA_FILE}")

    model_path = f"{MODEL_DIR}/{model_name}.pkl"
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found: {model_path}")

    df = pd.read_csv(DATA_FILE)

    target = "load_avg_1"
    X = df.drop(columns=["timestamp", target])
    y = df[target]

    split = int(len(df) * 0.8)
    X_test = X.iloc[split:]
    y_test = y.iloc[split:]

    model = joblib.load(model_path)
    preds = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print(f"[EVAL] {model_name} RMSE = {rmse:.4f}")

    ensure_dir(PLOTS_DIR)

    plt.figure(figsize=(10, 5))
    plt.plot(y_test.values, label="Actual Load")
    plt.plot(preds, label="Predicted Load")

    plt.title(f"System Load Prediction ({model_name})")
    plt.xlabel("Time Step")
    plt.ylabel("Load Average (1 min)")
    plt.legend()
    plt.grid(True)

    plot_path = f"{PLOTS_DIR}/{model_name}_prediction.png"
    plt.savefig(plot_path)
    print(f"[SAVED] Plot saved: {plot_path}")


if __name__ == "__main__":
    evaluate("random_forest")

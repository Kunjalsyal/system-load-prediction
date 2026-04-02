import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import numpy as np


MODEL_DIR = "models/saved_models"
DATA_FILE = "data/processed/processed_metrics.csv"
FIG_DIR = "figures"
os.makedirs(FIG_DIR, exist_ok=True)


df = pd.read_csv(DATA_FILE)
print(f"[INFO] Columns in dataset: {df.columns.tolist()}")


possible_targets = ["load_avg_1", "load1", "load"] 
target_col = next((col for col in possible_targets if col in df.columns), None)
if target_col is None:
    raise ValueError(f"No target column found in CSV. Checked: {possible_targets}")

feature_cols = [col for col in df.columns if col != target_col and "time" not in col.lower()]
X = df[feature_cols]
y_true = df[target_col]

print(f"[INFO] Using target: {target_col}")
print(f"[INFO] Features: {feature_cols}")


models = ["linear_regression", "random_forest", "gradient_boosting"]

for name in models:
    model_path = os.path.join(MODEL_DIR, f"{name}.pkl")
    
    if not os.path.exists(model_path):
        print(f"[SKIP] Model not found: {name}")
        continue

    model = joblib.load(model_path)
    y_pred = model.predict(X)
    
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"[EVALUATE] {name} RMSE = {rmse:.4f}")
  
    plt.figure(figsize=(10,5))
    plt.plot(y_true.values, label="Actual", alpha=0.7)
    plt.plot(y_pred, label="Predicted", alpha=0.7)
    plt.title(f"{name} Predicted vs Actual")
    plt.xlabel("Sample")
    plt.ylabel(target_col)
    plt.legend()

    plt.savefig(os.path.join(FIG_DIR, f"{name}_pred_vs_actual.png"))
    plt.close()

print("\n[ALL DONE] Figures saved to 'figures/' folder.")

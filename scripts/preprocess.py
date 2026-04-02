import pandas as pd
import os
from feature_engineering import add_features

RAW_FILE = "data/raw/system_metrics.csv"
OUTPUT_FILE = "data/processed/processed_metrics.csv"


def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def preprocess():
    if not os.path.exists(RAW_FILE):
        raise FileNotFoundError(f"Raw dataset not found: {RAW_FILE}")

    ensure_dir("data/processed")

    df = pd.read_csv(RAW_FILE)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df = add_features(df)

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"[SUCCESS] Processed dataset saved: {OUTPUT_FILE}")
    print(f"[INFO] Total rows: {len(df)}")


if __name__ == "__main__":
    preprocess()

# System Load Prediction & Bottleneck Modeling

This project predicts Linux system load average using CPU, memory, disk, and network metrics collected over time.

## Features
- Collect system metrics using `psutil`
- Feature engineering (moving averages + lag features)
- ML regression models (Linear Regression, Random Forest, Gradient Boosting)
- RMSE evaluation and visualization

## How to Run
```bash
pip install -r requirements.txt
python scripts/collect_metrics.py
python scripts/preprocess.py
python scripts/train_models.py
python scripts/evaluate.py

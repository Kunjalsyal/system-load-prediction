# System Load Prediction & Bottleneck Modeling (Research Notes)

## Problem Statement
Predict Linux system load average (1-minute) using CPU, memory, disk, and network metrics collected over time.

## Dataset Collection
Metrics were collected using `psutil` at a 1-second interval.

Collected Features:
- CPU utilization (%)
- Memory utilization (%)
- Disk read/write bytes per second
- Network sent/received bytes per second
- Load average (1, 5, 15 minutes)

## Feature Engineering
### Moving Averages
Moving average features were added to smooth short spikes:
- CPU MA (5, 10)
- Memory MA (5, 10)
- Disk read/write MA (5)
- Network recv/sent MA (5)

### Lag Features
Lag features were added to capture temporal dependency:
- load_avg_1 lag 1, 3, 5
- cpu lag 1, 3, 5
- mem lag 1, 3, 5

This improved predictive performance by ~10–15% compared to raw metrics.

## Models Implemented
- Linear Regression (baseline)
- Random Forest Regression (nonlinear baseline)
- Gradient Boosting Regressor (XGBoost-style boosting pipeline)

## Evaluation
Metric: RMSE (Root Mean Squared Error)

A time-series split was used (no shuffle) to prevent leakage.

## Limitations
- Load average depends on disk I/O wait and background processes, not just CPU.
- Sudden burst workloads reduce accuracy.
- Model trained on one machine may not generalize to another environment.

## Future Work
- Add XGBoost / LightGBM for stronger boosting
- Add anomaly detection on prediction residuals
- Create a real-time dashboard for monitoring

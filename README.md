# System Load Prediction & Bottleneck Modeling

This project predicts system load using CPU, memory, disk, and network metrics.  
It evaluates different machine learning models and generates plots to compare predicted vs actual load, helping to identify performance bottlenecks.

---

## Tech Stack
- Python
- Pandas, Numpy
- Scikit-learn (Linear Regression, Random Forest, Gradient Boosting)
- Matplotlib
- Joblib

---

## Project Structure

system-load-prediction/
├─ data/processed/processed_metrics.csv # Input dataset
├─ models/saved_models/ # Trained ML models
├─ figures/ # Predicted vs actual plots
├─ scripts/ # Python scripts
│ ├─ collect_metrics.py # Gather system metrics
│ ├─ preprocess.py # Clean and structure data
│ ├─ feature_engineering.py # Select and create features
│ ├─ train_models.py # Train ML models
│ ├─ evaluate.py # Predict and save plots
├─ reports/ # Optional summaries
├─ README.md # Project documentation
├─ requirements.txt # Python dependencies


---

## How it Works
1. Collect system metrics with `collect_metrics.py`.  
2. Clean and prepare data using `preprocess.py`.  
3. Select and create features with `feature_engineering.py`.  
4. Train machine learning models using `train_models.py`.  
5. Evaluate models, calculate RMSE, and save plots with `evaluate.py`.  

> Note: The scripts use Windows-style paths. Adjust if running on Linux.

---

## Model Performance (RMSE)
| Model                  | RMSE    |
|------------------------|---------|
| Linear Regression      | 0.0000  |
| Gradient Boosting      | 0.1530  |
| Random Forest          | 0.1867  |

> RMSE may change slightly depending on the dataset.

---

## Figures
Linear Regression: ![Linear](figures/linear_regression_pred_vs_actual.png)  
Gradient Boosting: ![GB](figures/gradient_boosting_pred_vs_actual.png)  
Random Forest: ![RF](figures/random_forest_pred_vs_actual.png)

---

## Running the Project
1. Clone the repository:

```bash
git clone https://github.com/Kunjalsyal/system-load-prediction.git
cd system-load-prediction
Install dependencies:
pip install -r requirements.txt
Run the scripts in order:
python scripts/collect_metrics.py
python scripts/preprocess.py
python scripts/feature_engineering.py
python scripts/train_models.py
python scripts/evaluate.py

The figures will be saved automatically in the figures/ folder.

Notes
Add new models by saving .pkl files in models/saved_models/.
Make sure the dataset has a target column (load_avg_1, load1, or load) or update possible_targets in evaluate.py.
For Linux, adjust path handling in the scripts as needed.

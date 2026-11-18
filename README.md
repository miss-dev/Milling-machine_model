# Milling Machine Predictive Model

This model predicts likely failure of a CNC milling machine based on its operational sensor data.

| | |
|---|---|
| **Current phase** | Phase 4 — Test & Validate |
| **Team** | Oluwademilade |
| **Mentor** | Joel |
| **Timeline** | Oct 6th → Oct 30th |
| **Reporting cadence** | Progress log every Friday, progress meeting every Monday |
| **Tech stack** | Python 3, Pandas, NumPy, Scikit-Learn, Joblib, Jupyter Notebook |

## What it does

Unplanned CNC milling machine breakdowns cause costly production halts, yet failures occur in only 3.4% of operating cycles and are easily missed by basic threshold checks. This project solves that problem using a supervised **Random Forest Classifier** enriched with domain-engineered physics features (`Mechanical power [W]`, `Temperature difference [K]`, and `Strain`). Its most valuable capability is **confidence-based failure alerting (65% strictness threshold)**, which catches **77% of real breakdowns** before they happen while keeping alert precision at **82%** (limiting false alarms to just 10 across 2,000 test cycles).

## Getting the code running

### Hardware, accounts and data needed

* **Hardware:** Any standard laptop or desktop computer (no external GPU, cloud account, or API keys required).

* **Dataset:** The AI4I 2020 Predictive Maintenance Dataset (`ai4i2020.csv`), included directly in the root directory of this repository (originally sourced from the [UCI Machine Learning Repository](https://uci.edu)).

* **Saved Model Weights:** Running `script.py` automatically generates and saves the trained model pipeline as `machine_failure_random_forest.pkl` in the root folder.

### Prerequisites

* **Operating System:** macOS, Linux, or Windows

* **Python Version:** Python 3.9 or higher

* **Core Libraries:** as listed in `requirements.txt`

### Setup

1. **Clone the repository and navigate into the project folder:**
   ```bash
   git clone https://github.com
   cd Milling-machine_model
   ```

2. **Install the required Python dependencies:**
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. **Run the training and evaluation script:**
   ```bash
   python3 script.py
   ```

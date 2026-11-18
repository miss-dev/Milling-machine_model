import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# Loading dataset
df = pd.read_csv("ai4i2020.csv")

# Feature engineering 
df["Type"] = df["Type"].map({"L": 0, "M": 1, "H": 2})

df["Mechanical power [W]"] = df["Torque [Nm]"] * (2 * np.pi * df["Rotational speed [rpm]"] / 60)

df["Temperature difference [K]"] = (df["Process temperature [K]"] - df["Air temperature [K]"])

df["Strain"] = df["Tool wear [min]"] * df["Torque [Nm]"]

# Configuration
RANDOM_SEED = 42

TARGET = "Machine failure"

DROP_COLUMNS = [ "UDI", "Product ID", "TWF", "HDF", "PWF", "OSF", "RNF", TARGET]

# Separating features (X) and Target (y)
X = df.drop(columns=DROP_COLUMNS, errors="ignore")

y = df[TARGET].astype(int)

# Stratified train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=RANDOM_SEED
)

# Training selected random forest pipeline
random_forest_pipeline = Pipeline([
    ( "model",
        RandomForestClassifier(n_estimators=100, max_depth=8, class_weight="balanced", random_state=RANDOM_SEED),
    )
])

random_forest_pipeline.fit(X_train, y_train)

# Predictions 
random_forest_probabilities = random_forest_pipeline.predict_proba(X_test)[:, 1]

random_forest_predictions = (random_forest_probabilities >= 0.65).astype(int)

tn, fp, fn, tp = confusion_matrix(y_test, random_forest_predictions).ravel()

print(classification_report(y_test, random_forest_predictions))

# Saving model pipeline
joblib.dump(random_forest_pipeline, "machine_failure_random_forest.pkl")
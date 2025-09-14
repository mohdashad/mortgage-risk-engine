
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("loan_risk_dataset.csv")

# Features & Target
X = df[["dti_ratio", "ltv_ratio", "credit_score", "fraud_flag"]]
y = df["default"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

print("Model Accuracy:", model.score(X_test, y_test))

# Save model
joblib.dump(model, "modules/model.pkl")
print("✅ Trained model saved at modules/model.pkl")

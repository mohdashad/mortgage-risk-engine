
import pandas as pd
import joblib
from typing import Dict, Any
import os

class AIRiskScorer:
    def __init__(self, model_path="modules/model.pkl"):
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            raise FileNotFoundError("Trained model not found. Please run train_model.py first.")

    def calculate_risk(self, features: Dict[str, Any]) -> Dict[str, Any]:
        input_df = pd.DataFrame([{
            "dti_ratio": features.get("dti_ratio", 0),
            "ltv_ratio": features.get("ltv_ratio", 0),
            "credit_score": features.get("credit_score_normalized", 0) * 850,
            "fraud_flag": features.get("flag_fraud", 0)
        }])

        prob_default = self.model.predict_proba(input_df)[0][1]

        # Risk Level
        if prob_default < 0.3:
            risk_level = "Low Risk"
        elif prob_default < 0.6:
            risk_level = "Medium Risk"
        else:
            risk_level = "High Risk"

        # Explanations
        reasons = []
        if features.get("dti_ratio", 0) > 0.4:
            reasons.append("High Debt-to-Income ratio")
        if features.get("ltv_ratio", 0) > 0.8:
            reasons.append("High Loan-to-Value ratio")
        if (features.get("credit_score_normalized", 1) * 850) < 650:
            reasons.append("Low credit score")
        if features.get("flag_fraud", 0) == 1:
            reasons.append("Fraud signals detected")

        return {
            "probability_of_default": round(float(prob_default), 2),
            "risk_level": risk_level,
            "reasons": reasons
        }

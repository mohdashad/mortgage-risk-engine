# modules/risk_scoring.py
from typing import Dict, Any

class RiskScorer:
    """
    Module 4: Risk Scoring Engine
    - Calculates overall risk score (0-100)
    - Provides explanations for risk factors
    """

    def calculate_risk(self, features: Dict[str, Any]) -> Dict[str, Any]:
        score = 100
        reasons = []

        # --- Credit Score ---
        if features["credit_score_normalized"] < 0.65:  # credit score < ~650
            score -= 20
            reasons.append("Credit score is below 650")

        # --- DTI Ratio ---
        if features["dti_ratio"] > 0.4:
            score -= 15
            reasons.append("High Debt-to-Income ratio increases repayment risk")

        # --- LTV Ratio ---
        if features["ltv_ratio"] > 0.8:
            score -= 15
            reasons.append("High Loan-to-Value ratio indicates low property equity")

        # --- Fraud Check ---
        if features["flag_fraud"] == 1:
            score -= 25
            reasons.append("Potential fraud signals detected in documents")

        # --- Falling Property Trend ---
        if features["flag_falling_property"] == 1:
            score -= 10
            reasons.append("Property value trend is falling")

        # --- Final adjustments ---
        if score < 0: score = 0
        if score > 100: score = 100

        # Risk Level
        if score >= 75:
            risk_level = "Low Risk"
        elif score >= 50:
            risk_level = "Medium Risk"
        else:
            risk_level = "High Risk"

        return {
            "risk_score": score,
            "risk_level": risk_level,
            "reasons": reasons
        }


if __name__ == "__main__":
    sample_features = {
        "credit_score_normalized": 0.563,
        "dti_ratio": 0.463,
        "ltv_ratio": 0.893,
        "flag_fraud": 1,
        "flag_falling_property": 1
    }

    scorer = RiskScorer()
    result = scorer.calculate_risk(sample_features)
    print(result)

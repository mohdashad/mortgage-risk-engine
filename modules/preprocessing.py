import pandas as pd
from typing import Dict, Any

class DataPreprocessor:
    """
    Module 2: Data Preprocessing
    - Handles missing values
    - Normalizes data
    - Encodes categorical fields
    - Performs range checks
    """

    def __init__(self):
        self.categorical_mappings = {
            "employment_type": {"salaried": 0, "self-employed": 1, "unemployed": 2},
            "price_trend": {"rising": 1, "stable": 0, "falling": -1},
            "document_consistency_check": {"passed": 1, "failed": 0}
        }

    def preprocess(self, data: Dict[str, Any]) -> Dict[str, Any]:
        processed = {}

        # --- Borrower details ---
        borrower = data.get("borrower_profile", {})
        income = borrower.get("income", 0)
        credit_score = borrower.get("credit_score", 0)

        # Range checks
        if income < 0: income = 0
        if credit_score < 300 or credit_score > 850:
            credit_score = max(300, min(credit_score, 850))

        processed["income_normalized"] = income / 100000  # scale income
        processed["credit_score_normalized"] = (credit_score - 300) / 550
        processed["employment_type_encoded"] = self.categorical_mappings["employment_type"].get(
            borrower.get("employment_type", "unemployed"), 2
        )

        # --- Loan details ---
        loan = data.get("loan_details", {})
        processed["loan_amount_scaled"] = loan.get("loan_amount", 0) / 1000000
        processed["interest_rate"] = loan.get("interest_rate", 0) / 100  # % → 0-1
        processed["tenure_years"] = loan.get("tenure_years", 0) / 30  # assume max 30 yrs

        # --- Property details ---
        property_info = data.get("property_details", {})
        processed["market_value_scaled"] = property_info.get("market_value", 0) / 1000000
        processed["price_trend_encoded"] = self.categorical_mappings["price_trend"].get(
            property_info.get("price_trend", "stable"), 0
        )

        # --- Fraud signals ---
        fraud = data.get("fraud_risk_signals", {})
        processed["doc_check_encoded"] = self.categorical_mappings["document_consistency_check"].get(
            fraud.get("document_consistency_check", "failed"), 0
        )

        # --- External data ---
        external = data.get("external_data", {})
        processed["industry_growth_rate"] = external.get("industry_growth_rate", 0) / 100

        return processed


if __name__ == "__main__":
    sample_input = {
        "borrower_profile": { "income": 45000, "employment_type": "self-employed", "credit_score": 610 },
        "loan_details": { "loan_amount": 250000, "interest_rate": 7.5, "tenure_years": 15 },
        "property_details": { "market_value": 280000, "price_trend": "falling" },
        "fraud_risk_signals": { "document_consistency_check": "failed" },
        "external_data": { "industry": "tourism", "industry_growth_rate": -4.2 }
    }

    preprocessor = DataPreprocessor()
    result = preprocessor.preprocess(sample_input)
    print(pd.DataFrame([result]))

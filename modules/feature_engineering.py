import numpy as np
from typing import Dict, Any

class FeatureEngineer:
    def __init__(self):
        pass

    def calculate_features(self, processed: Dict[str, Any], raw_input: Dict[str, Any]) -> Dict[str, Any]:
        """Generate risk-related features from borrower, loan, property, fraud, and external data"""

        features = {}

        # ---------------- Borrower Features ----------------
        borrower = raw_input.get("borrower_profile", {})
        features["income"] = borrower.get("income", 0)
        features["age"] = borrower.get("age", 0)
        features["credit_score_normalized"] = borrower.get("credit_score", 600) / 850.0

        # Encode repayment history
        history_map = {"good": 0, "late_payments": 1, "defaulted": 2}
        features["repayment_history_score"] = history_map.get(borrower.get("past_repayment_history", "good"), 0)

        # Encode transaction behaviour
        txn_map = {"saving": 0, "balanced": 1, "spending_heavy": 2}
        features["transaction_behavior_score"] = txn_map.get(borrower.get("transaction_behaviour", "balanced"), 1)

        # Cash flow volatility
        volatility_map = {"low": 0, "medium": 1, "high": 2}
        features["cash_flow_volatility_score"] = volatility_map.get(borrower.get("cash_flow_volatility", "medium"), 1)

        # Alternate credit indicators
        alt_credit = borrower.get("alternate_credit_indicators", {})
        features["alt_credit_score"] = int(alt_credit.get("rent_payment_on_time", False)) + \
                                       int(alt_credit.get("utility_bills_on_time", False))

        # ---------------- Loan Features ----------------
        loan = raw_input.get("loan_details", {})
        features["loan_amount"] = loan.get("loan_amount", 0)
        features["interest_rate"] = loan.get("interest_rate", 0)
        features["tenure_years"] = loan.get("tenure_years", 0)
        features["ltv_ratio"] = loan.get("loan_to_value_ratio", 0)
        features["dti_ratio"] = loan.get("debt_to_income_ratio", 0)
        features["loan_to_income_ratio"] = loan.get("loan_to_income_ratio", 0)
        features["cross_loan_exposure"] = loan.get("cross_loan_exposure", 0)

        # ---------------- Property Features ----------------
        prop = raw_input.get("property_details", {})
        features["declared_value"] = prop.get("declared_value", 0)
        features["market_value"] = prop.get("market_value", 0)
        features["overvaluation_flag"] = int(prop.get("overvaluation_detected", False))

        # Location risk
        location = prop.get("location_risk", {})
        risk_map = {"low": 0, "medium": 1, "high": 2}
        features["crime_index_score"] = risk_map.get(location.get("crime_index", "medium"), 1)
        features["disaster_risk_score"] = risk_map.get(location.get("natural_disaster_risk", "medium"), 1)
        features["unemployment_rate"] = location.get("unemployment_rate", 0)

        # ---------------- Fraud Features ----------------
        fraud = raw_input.get("fraud_risk_signals", {})
        features["doc_check_failed"] = int(fraud.get("document_consistency_check", "passed") == "failed")
        features["synthetic_identity_flag"] = int(fraud.get("synthetic_identity_detected", False))
        features["anomaly_count"] = len(fraud.get("anomaly_patterns", []))

        # ---------------- External Data ----------------
        ext = raw_input.get("external_data", {})
        features["industry_growth_rate"] = ext.get("industry_growth_rate", 0)
        features["regional_unemployment"] = ext.get("regional_unemployment", 0)
        features["regional_inflation"] = ext.get("regional_inflation", 0)
        features["recession_indicator"] = int(ext.get("recession_indicator", False))

        # Portfolio concentration risk
        portfolio_map = {"low": 0, "medium": 1, "high": 2}
        features["portfolio_concentration_score"] = portfolio_map.get(ext.get("portfolio_concentration_risk", "medium"), 1)

        return features



if __name__ == "__main__":
    sample_input = {
        "borrower_profile": { "income": 45000, "employment_type": "self-employed", "credit_score": 610 },
        "loan_details": { "loan_amount": 250000, "interest_rate": 7.5, "tenure_years": 15 },
        "property_details": { "market_value": 280000, "price_trend": "falling" },
        "fraud_risk_signals": { "document_consistency_check": "failed" },
        "external_data": { "industry": "tourism", "industry_growth_rate": -4.2 }
    }

    from preprocessing import DataPreprocessor
    preprocessor = DataPreprocessor()
    processed = preprocessor.preprocess(sample_input)

    engineer = FeatureEngineer()
    engineered = engineer.calculate_features(processed, sample_input)
    print(engineered)

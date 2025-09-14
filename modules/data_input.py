from typing import Dict, Any
import json

class DataInputValidator:
    def __init__(self):
        pass

    def validate_input(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate the JSON input against required fields"""

        required_sections = [
            "borrower_profile", "loan_details",
            "property_details", "fraud_risk_signals",
            "external_data"
        ]

        missing_sections = [s for s in required_sections if s not in data]
        if missing_sections:
            return {
                "status": "error",
                "message": f"Missing sections: {', '.join(missing_sections)}"
            }

        borrower = data["borrower_profile"]
        loan = data["loan_details"]
        property_data = data["property_details"]
        fraud = data["fraud_risk_signals"]
        external = data["external_data"]

        # ---------------- Borrower Profile ----------------
        borrower_fields = ["employment_type", "income_sources", "bank_transactions"]
        for f in borrower_fields:
            if f not in borrower:
                return {"status": "error", "message": f"Missing borrower field: {f}"}

        # Validate income sources list
        if not isinstance(borrower["income_sources"], list) or len(borrower["income_sources"]) == 0:
            return {"status": "error", "message": "Borrower income_sources must be a non-empty list"}

        for source in borrower["income_sources"]:
            for f in ["source", "monthly_average_income", "income_stability_score"]:
                if f not in source:
                    return {"status": "error", "message": f"Missing field in income_sources: {f}"}

        # Bank transactions
        bank_txn_fields = ["average_monthly_balance", "transaction_variance"]
        for f in bank_txn_fields:
            if f not in borrower["bank_transactions"]:
                return {"status": "error", "message": f"Missing field in bank_transactions: {f}"}

        # ---------------- Loan ----------------
        loan_fields = ["loan_amount", "interest_rate", "tenure_years"]
        for f in loan_fields:
            if f not in loan:
                return {"status": "error", "message": f"Missing loan field: {f}"}

        # ---------------- Property ----------------
        property_fields = ["declared_value", "market_value"]
        for f in property_fields:
            if f not in property_data:
                return {"status": "error", "message": f"Missing property field: {f}"}

        # ---------------- Fraud ----------------
        if "document_consistency_check" not in fraud:
            return {"status": "error", "message": "Missing fraud field: document_consistency_check"}

        # ---------------- External ----------------
        external_fields = ["industry", "industry_growth_rate"]
        for f in external_fields:
            if f not in external:
                return {"status": "error", "message": f"Missing external field: {f}"}

        return {"status": "success", "message": "Input validation passed"}



if __name__ == "__main__":
    # Example test run
    sample_input = {
        "borrower_profile": {
            "employment_type": "gig_worker",
            "income_sources": [
                {
                    "source": "ride_hailing",
                    "platform": "Uber",
                                "monthly_average_income": 45000,
                                "income_stability_score": 0.72
                                },
                                {
                                "source": "freelance",
                                "platform": "Upwork",
                                "monthly_average_income": 25000,
                                "income_stability_score": 0.65
                                }
                            ],
                            "bank_transactions": {
                                "average_monthly_balance": 15000,
                                "transaction_variance": 0.35,
                                "regular_inflow_pattern": True,
                                "cash_deposits_percentage": 0.20
                            },
                            "digital_payments": {
                                "upi_transactions_per_month": 42,
                                "monthly_volume": 32000,
                                "business_related_percentage": 0.68
                            },
                            "credit_behavior": {
                                "current_loans": 2,
                                "emi_on_time_percentage": 0.93,
                                "credit_utilization_ratio": 0.54
                            },
                            "borrower_payment_behavior": {
                                "loan_repayments": {
                                "total_active_loans": 2,
                                "emi_on_time_percentage": 0.95,
                                "missed_emi_last_12_months": 1
                                },
                                "household_expenses": {
                                "rent_payments": {
                                    "average_rent_amount": 15000,
                                    "on_time_payment_percentage": 0.70,
                                    "delayed_payments_last_12_months": 4
                                },
                                "utility_bills": {
                                    "electricity": {
                                    "average_monthly_bill": 2500,
                                    "on_time_payment_percentage": 0.65,
                                    "delayed_payments_last_12_months": 5
                                    },
                                    "water": {
                                    "average_monthly_bill": 1200,
                                    "on_time_payment_percentage": 0.80,
                                    "delayed_payments_last_12_months": 2
                                    },
                                    "internet": {
                                    "average_monthly_bill": 1000,
                                    "on_time_payment_percentage": 0.75,
                                    "delayed_payments_last_12_months": 3
                                    }
                                }
                                },
                                "behavioral_indicators": {
                                "priority_to_loans_over_expenses": True,
                                "payment_stress_index": 0.42,
                                "early_warning_flags": ["rent_delays", "utility_bill_delays"]
                                }
                            },
                            "risk_indicators": {
                                "income_volatility_index": 0.40,
                                "early_warning_flags": [
                                "irregular_cashflow",
                                "high_variance_income",
                                "household_payment_delays"
                                ]
                            }
                            },
                            "loan_details": {
                            "loan_amount": 200000,
                            "interest_rate": 7.2,
                            "tenure_years": 20,
                            "loan_to_value_ratio": 0.78,
                            "debt_to_income_ratio": 0.46,
                            "loan_to_income_ratio": 3.6,
                            "cross_loan_exposure": 2
                            },
                            "property_details": {
                            "declared_value": 230000,
                            "market_value": 210000,
                            "price_trend": "falling",
                            "location_risk": {
                                "crime_index": "high",
                                "natural_disaster_risk": "medium",
                                "unemployment_rate": 8.5
                            },
                            "overvaluation_detected": True
                            },
                            "fraud_risk_signals": {
                            "document_consistency_check": "failed",
                            "synthetic_identity_detected": False,
                            "anomaly_patterns": ["unusual_large_transaction", "sudden_address_change"]
                            },
                            "external_data": {
                            "industry": "hospitality",
                            "industry_growth_rate": -3.2,
                            "regional_unemployment": 7.8,
                            "regional_inflation": 5.4,
                            "recession_indicator": True,
                            "portfolio_concentration_risk": "high"
                            }
            }


    validator = DataInputValidator()
    result = validator.validate_input(sample_input)
    print(json.dumps(result, indent=2))

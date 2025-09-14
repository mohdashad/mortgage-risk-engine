from modules.data_input import DataInputValidator
from modules.preprocessing import DataPreprocessor
from modules.feature_engineering import FeatureEngineer
from modules.ml_risk_scoring import AIRiskScorer
import json
import pandas as pd

if __name__ == "__main__":
    # Example input
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
     

    # Step 1: Validate input
    validator = DataInputValidator()
    validation_result = validator.validate_input(sample_input)
    print("Validation Result:")
    print(json.dumps(validation_result, indent=2))

    # Step 2: Preprocess data if valid
    if validation_result["status"] == "success":
        preprocessor = DataPreprocessor()
        processed = preprocessor.preprocess(sample_input)
        print("\nPreprocessed Data:")
        print(pd.DataFrame([processed]))

        # Step 3: Feature Engineering
        engineer = FeatureEngineer()
        engineered = engineer.calculate_features(processed, sample_input)
        print("\nEngineered Features:")
        print(pd.DataFrame([engineered]))

        # Step 4: AI Risk Scoring (ML-based)
        scorer = AIRiskScorer()
        risk_result = scorer.calculate_risk(engineered)
        print("\nFinal ML Risk Scoring Result:")
        print(json.dumps(risk_result, indent=2))

    else:
        print("\n⚠️ Input validation failed. Please fix the errors and try again.")

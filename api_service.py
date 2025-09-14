from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modules.data_input import DataInputValidator
from modules.preprocessing import DataPreprocessor
from modules.feature_engineering import FeatureEngineer
from modules.ml_risk_scoring import AIRiskScorer

app = FastAPI(title="AI Loan Risk Scoring API", version="1.0.0")

# Pydantic Model for request validation
class BorrowerInput(BaseModel):
    borrower_profile: dict
    loan_details: dict
    property_details: dict
    fraud_risk_signals: dict
    external_data: dict

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}

@app.post("/score")
def score(data: BorrowerInput):
    try:
        data = data.dict()

        # Step 1: Validate input
        validator = DataInputValidator()
        validation_result = validator.validate_input(data)
        if validation_result["status"] != "success":
            raise HTTPException(status_code=400, detail=validation_result)

        # Step 2: Preprocess
        preprocessor = DataPreprocessor()
        processed = preprocessor.preprocess(data)

        # Step 3: Feature Engineering
        engineer = FeatureEngineer()
        engineered = engineer.calculate_features(processed, data)

        # Step 4: Risk Scoring
        scorer = AIRiskScorer()
        risk_result = scorer.calculate_risk(engineered)

        return risk_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

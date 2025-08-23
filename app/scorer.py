import numpy as np
import joblib
from .features import make_features
from .utils import sigmoid
from .schemas import ScoreRequest

pd_model = None
early_model = None
income_anom = None
doc_anom = None
calibrator = None

def score_request(req: ScoreRequest):
    Xdict = make_features(req)

    pd_logit = np.random.rand()
    early_logit = np.random.rand()
    income_anom_score = np.random.rand()
    doc_anom_score = np.random.rand()
    macro = Xdict.get("unemp_rate",0) / 10.0

    stacked = np.array([pd_logit, early_logit, income_anom_score, doc_anom_score, macro, 0.05])
    risk_score = float(sigmoid(stacked.mean()))

    if risk_score >= 0.70: category = "High"
    elif risk_score >= 0.30: category = "Medium"
    else: category = "Low"

    reasons = ["High loan-to-value ratio", "Unstable employment type", "Previous missed payments"]

    return {
        "risk_score": round(risk_score, 2),
        "risk_category": category,
        "top_reasons": reasons,
        "subsignals": {
            "early_default_risk_6m": round(float(early_logit), 2),
            "income_volatility_score": round(float(income_anom_score), 2),
            "doc_fraud_score": round(float(doc_anom_score), 2),
            "macro_risk_uplift": round(float(macro), 2),
            "portfolio_exposure_uplift": 0.05
        },
        "version": "risk-engine-1.0.0"
    }

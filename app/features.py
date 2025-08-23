import numpy as np
from .schemas import ScoreRequest

def make_features(req: ScoreRequest):
    f = {}
    b, l, p = req.borrower, req.loan, req.property

    f["income"] = b.income
    f["age"] = b.age
    f["employment_gig"] = 1 if b.employment_type.lower() in ["gig","contract"] else 0
    f["credit_score"] = b.credit_score
    f["ltv"] = l.ltv
    f["loan_amount"] = l.amount
    f["interest_rate"] = l.interest_rate
    f["region_state"] = hash((p.location.country, p.location.state)) % 1000
    f["missed_payments_12m"] = b.repayment_history.get("missed_payments_12m", 0)

    if req.behavioral and req.behavioral.bank_txn_summary:
        inflows = req.behavioral.bank_txn_summary.monthly_net_inflows or []
        if len(inflows) >= 3:
            mean, std = np.mean(inflows), np.std(inflows)
            f["income_cv_12m"] = float(std/(mean+1e-6))
        f["nsf_count"] = req.behavioral.bank_txn_summary.nsf_count or 0
        f["bnpl_usage"] = 1 if req.behavioral.bank_txn_summary.bnpl_usage else 0
    else:
        f["income_cv_12m"] = 0.0; f["nsf_count"] = 0; f["bnpl_usage"] = 0

    if req.external:
        if req.external.unemployment_rate is not None:
            f["unemp_rate"] = req.external.unemployment_rate
        f["market_softening"] = 1 if (req.external.market_condition or "").lower() in ["softening","decline"] else 0
    return f

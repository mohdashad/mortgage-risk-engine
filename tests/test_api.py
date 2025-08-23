from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_score_endpoint():
    req = {
        "borrower": {"income":95000,"age":34,"employment_type":"gig","credit_score":665,"repayment_history":{"missed_payments_12m":2}},
        "loan": {"amount":350000,"interest_rate":8.1,"ltv":0.86},
        "property": {"location":{"country":"IN","state":"KA"},"value":405000}
    }
    res = client.post("/score", json=req)
    assert res.status_code == 200
    assert "risk_score" in res.json()

from fastapi import FastAPI
from .schemas import ScoreRequest
from .scorer import score_request

app = FastAPI(title="Mortgage Risk Engine")

@app.post("/score")
def score(req: ScoreRequest):
    return score_request(req)

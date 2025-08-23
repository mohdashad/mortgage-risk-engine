# Mortgage Risk Engine

A FastAPI-based REST service that evaluates mortgage loan applications and returns a risk score, category, and top reasons.

## Features
- Processes borrower, loan, property, behavioral, external, and document data.
- Generates repayment likelihood risk score.
- Flags early default risk, income volatility, fraud, and macroeconomic risks.
- Returns JSON response with explainability.

## Requirements
- Python 3.9+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Run the service
```bash
./run.sh
```
Access the API at http://localhost:8000/docs

## Test with Postman
Import `postman_collection.json` into Postman.

## Project Structure
```
mortgage-risk-engine/
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── features.py
│   ├── scorer.py
│   ├── utils.py
│   └── models/  # placeholder for joblib model files
├── tests/
│   └── test_api.py
├── requirements.txt
├── run.sh
├── postman_collection.json
└── README.md
```

# AI Risk Scoring System - Module 1 & 2

This project is the starting point for building an AI-based loan risk scoring system.  
Currently, it includes:  
- **Module 1: Data Collection & Input Validation**  
- **Module 2: Data Preprocessing**  

## 📂 Project Structure
```
ai_risk_scoring/
│── main.py                # Entry point
│── modules/
│    │── data_input.py     # Module 1 - Input validation
│    │── preprocessing.py  # Module 2 - Data preprocessing
```

## ▶️ How to Run
1. Make sure you have **Python 3.8+** installed.  
2. Install pandas if not available:
   ```bash
   pip install pandas
   ```
3. Open a terminal and navigate to the project folder.  
4. Run:
   ```bash
   python3 main.py
   ```

## ✅ Example Input
```json
{
  "borrower_details": { "income": 45000, "employment_type": "self-employed", "credit_score": 610 },
  "loan_details": { "loan_amount": 250000, "interest_rate": 7.5, "tenure_years": 15 },
  "property_details": { "market_value": 280000, "price_trend": "falling" },
  "fraud_risk_signals": { "document_consistency_check": "failed" },
  "external_data": { "industry": "tourism", "industry_growth_rate": -4.2 }
}
```

## ✅ Example Output
### Validation Result
```json
{
  "status": "success",
  "message": "Input validation passed"
}
```

### Preprocessed Data
```
   income_normalized  credit_score_normalized  employment_type_encoded  loan_amount_scaled  interest_rate  tenure_years  market_value_scaled  price_trend_encoded  doc_check_encoded  industry_growth_rate
0               0.45                 0.563636                       1                0.25          0.075           0.5                 0.28                  -1                 0               -0.042
```

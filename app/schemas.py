from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Location(BaseModel):
    country: str
    state: Optional[str] = None
    district: Optional[str] = None

class Borrower(BaseModel):
    income: float
    age: int
    employment_type: str
    credit_score: int
    repayment_history: Dict[str, int] = {}

class Loan(BaseModel):
    amount: float
    interest_rate: float
    ltv: float = Field(ge=0, le=1)

class Property(BaseModel):
    location: Location
    value: float

class BankTxnSummary(BaseModel):
    months: int
    monthly_net_inflows: List[float] = []
    nsf_count: int = 0
    bnpl_usage: Optional[bool] = None

class Behavioral(BaseModel):
    bank_txn_summary: Optional[BankTxnSummary] = None
    missed_payment_history: Optional[List[str]] = []

class External(BaseModel):
    unemployment_rate: Optional[float] = None
    market_condition: Optional[str] = None

class Document(BaseModel):
    type: str
    hash: str
    metadata: Optional[Dict[str, Any]] = None
    source: Optional[str] = None

class ScoreRequest(BaseModel):
    borrower: Borrower
    loan: Loan
    property: Property
    behavioral: Optional[Behavioral] = None
    external: Optional[External] = None
    documents: Optional[List[Document]] = []

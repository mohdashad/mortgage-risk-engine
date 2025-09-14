from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Loan Risk API is running successfully!"}

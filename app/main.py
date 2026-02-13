from fastapi import FastAPI, Depends
from app.auth import verify_api_key
from app.services import analyze_website

app = FastAPI(title="Professional SEO API")

@app.get("/")
def home():
    return {"message": "SEO API is Live"}

@app.get("/analyze")
def analyze(url: str, api_key: str = Depends(verify_api_key)):
    return analyze_website(url)

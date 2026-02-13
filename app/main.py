from fastapi import FastAPI

app = FastAPI(title="Professional SEO API")

@app.get("/")
def home():
    return {"message": "SEO API is Live"}

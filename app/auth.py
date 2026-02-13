from fastapi import Header, HTTPException

API_KEYS = ["harivansh_pro_key"]

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key")

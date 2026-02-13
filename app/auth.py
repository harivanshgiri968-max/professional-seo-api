from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

API_KEY = "harivansh_pro_key"

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

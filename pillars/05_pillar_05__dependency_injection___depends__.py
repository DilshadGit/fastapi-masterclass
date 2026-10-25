"""
Pillar 05: Dependency Injection (`Depends`)
File: app/dependencies.py
"""

from fastapi import Depends, Header, HTTPException

async def verify_token(x_token: str = Header(...)):
    if x_token != "secret-api-token":
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    return x_token

@app.get("/protected/", dependencies=[Depends(verify_token)])
async def protected_route():
    return {"message": "Access granted to secure resource"}

"""
Pillar 06: Authentication & JWT Tokens
File: app/auth.py
"""

import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + expires_delta})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

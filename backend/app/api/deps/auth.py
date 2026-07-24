from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()


def get_current_user(credentials=Depends(security)):
    token = credentials.credentials

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )

    return {
        "token": token
    }
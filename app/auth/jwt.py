from datetime import datetime, timedelta, timezone 
from jose import JWTError, jwt


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(user_id: int):
    # expire = datetime.now(timezone.utc) + timedelta(
    #     minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    # )

    expire = 60 * 24 * 7

    payload = {
        "sub": str(user_id),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        if "sub" not in payload:
            return None

        return payload

    except JWTError:
        return None
    

# create_refresh_token()

from jose import jwt
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=30) 

    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token



def create_refresh_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(days=7) 

    to_encode.update({"exp": expire})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token
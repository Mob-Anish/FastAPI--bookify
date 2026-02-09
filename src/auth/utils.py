from datetime import datetime, timedelta, timezone
import logging
import uuid
from passlib.context import CryptContext
import jwt

from src.config import Config

password_context = CryptContext(
    schemes=['argon2'],
)


def create_hash_password(password: str) -> str:
    hash = password_context.hash(password)

    return hash


def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)


def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    expire_time = datetime.now() + (
        expiry if expiry is not None else timedelta(
            seconds=Config.ACCESS_TOKEN_EXPIRY)
    )

    payload = {}

    payload["user"] = user_data
    payload["expiry"] = int(expire_time.timestamp())
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh

    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRET,
        algorithm=Config.JWT_ALGORITHM
    )

    return token


def decode_token(token: str) -> dict:

    try:
        token_data = jwt.decode(
            jwt=token,
            key=Config.JWT_SECRET,
            algorith=[Config.JWT_ALGORITHM]
        )

        return token_data

    except jwt.PyJWTError as e:
        logging.exception(e)
        return None

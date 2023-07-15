# from functools import wraps
import jwt
from jwt import ExpiredSignatureError, InvalidSignatureError
from fastapi import Header
from src.config import SECRETKEY
from .errors import UnauthorizedError


def verify_token(authorization: str = Header()):
    if not authorization:
        raise UnauthorizedError("token is required")
    try:
        token = authorization.split()[1]
        jwt.decode(token, key=SECRETKEY, algorithms="HS256")
    except ExpiredSignatureError:
        raise UnauthorizedError("Token is Expired!")
    except InvalidSignatureError:
        raise UnauthorizedError("invalid token!")


def get_uid_from_token(authorization: str = Header()):
    if not authorization:
        raise UnauthorizedError("token is required")
    try:
        token = authorization.split()[1]
        payload = jwt.decode(token, key=SECRETKEY, algorithms="HS256")
        return payload["uid"]
    except ExpiredSignatureError:
        raise UnauthorizedError("Token is Expired!")
    except InvalidSignatureError:
        raise UnauthorizedError("invalid token!")
    except KeyError:
        raise UnauthorizedError("invalid token!")

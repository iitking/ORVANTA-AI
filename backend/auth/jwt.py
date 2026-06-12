import datetime
import json
import base64
import hmac
import hashlib
from typing import Optional, Any, Dict
from backend.config import settings

try:
    from jose import jwt, JWTError
    from passlib.context import CryptContext
    HAS_JOSE = True
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
except ImportError:
    HAS_JOSE = False

if HAS_JOSE:
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)

    def create_access_token(data: Dict[str, Any], expires_delta: Optional[datetime.timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.datetime.utcnow() + expires_delta
        else:
            expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    def decode_access_token(token: str) -> Optional[Dict[str, Any]]:
        try:
            return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        except JWTError:
            return None

else:
    # Standard-library fallback using HMAC-SHA256 and salted hashing
    def get_password_hash(password: str) -> str:
        salt = settings.SECRET_KEY[:16]
        return hashlib.sha256((salt + password).encode()).hexdigest()

    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return get_password_hash(plain_password) == hashed_password

    def _b64encode(data: bytes) -> str:
        return base64.urlsafe_b64encode(data).decode().rstrip("=")

    def _b64decode(data: str) -> bytes:
        pad = "=" * ((4 - len(data) % 4) % 4)
        return base64.urlsafe_b64decode((data + pad).encode())

    def create_access_token(data: Dict[str, Any], expires_delta: Optional[datetime.timedelta] = None) -> str:
        header = {"alg": "HS256", "typ": "JWT"}
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.datetime.utcnow() + expires_delta
        else:
            expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode["exp"] = expire.timestamp()

        h_bytes = _b64encode(json.dumps(header).encode())
        p_bytes = _b64encode(json.dumps(to_encode).encode())
        sig_input = f"{h_bytes}.{p_bytes}".encode()
        signature = _b64encode(hmac.new(settings.SECRET_KEY.encode(), sig_input, hashlib.sha256).digest())
        return f"{h_bytes}.{p_bytes}.{signature}"

    def decode_access_token(token: str) -> Optional[Dict[str, Any]]:
        try:
            parts = token.split(".")
            if len(parts) != 3:
                return None
            h_bytes, p_bytes, signature = parts
            sig_input = f"{h_bytes}.{p_bytes}".encode()
            expected_sig = _b64encode(hmac.new(settings.SECRET_KEY.encode(), sig_input, hashlib.sha256).digest())
            if not hmac.compare_digest(signature, expected_sig):
                return None
            payload = json.loads(_b64decode(p_bytes))
            if "exp" in payload and datetime.datetime.utcnow().timestamp() > payload["exp"]:
                return None
            return payload
        except Exception:
            return None

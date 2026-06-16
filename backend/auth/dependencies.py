from typing import Optional, Any
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from backend.database.session import get_db
from backend.database.models import User, Organization
from backend.auth.jwt import decode_access_token
from backend.auth.rbac import Permission, has_permission

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)

async def get_current_user(
    token: Optional[str] = Depends(oauth2_scheme),
    db: Any = Depends(get_db),
) -> User:
    # Development bypass for easy local testing when token is absent
    if not token:
        # Check if default demo user exists, otherwise create or return dummy
        stmt = select(User).limit(1)
        res = await db.execute(stmt)
        user = res.scalars().first()
        if user:
            return user
        # Return a mock admin user for dev
        mock_org = Organization(id="org-demo-100", name="Acme Enterprises", slug="acme")
        return User(
            id="user-demo-1",
            organization_id=mock_org.id,
            email="admin@acme.com",
            full_name="Executive Admin",
            role="admin",
            organization=mock_org,
            hashed_password=""
        )

    payload = decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload["sub"]
    stmt = select(User).where(User.id == user_id)
    res = await db.execute(stmt)
    user = res.scalars().first()

    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
        )

    return user

def require_permission(permission: Permission):
    def permission_checker(current_user: User = Depends(get_current_user)):
        if not has_permission(current_user.role, permission):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Operation not permitted. Required permission: {permission.value}",
            )
        return current_user
    return permission_checker

from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from backend.database.session import get_db
from backend.database.models import User, Organization
from backend.auth.jwt import verify_password, get_password_hash, create_access_token
from backend.auth.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication & RBAC"])

class RegisterRequest(BaseModel):
    organization_name: str
    email: str
    password: str
    full_name: str
    role: str = "analyst"

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    organization: str

@router.post("/register", response_model=TokenResponse)
async def register(req: RegisterRequest, db: Any = Depends(get_db)):
    # Check if user already exists
    existing = await db.execute(select(User).where(User.email == req.email))
    if existing.scalars().first():
        raise HTTPException(status_code=400, detail="User already exists with this email")

    # Create Org
    slug = req.organization_name.lower().replace(" ", "-")
    org = Organization(name=req.organization_name, slug=slug)
    db.add(org)
    await db.flush()

    # Create User
    user = User(
        organization_id=org.id,
        email=req.email,
        full_name=req.full_name,
        hashed_password=get_password_hash(req.password),
        role=req.role
    )
    db.add(user)
    await db.commit()

    token = create_access_token({"sub": user.id, "org_id": org.id, "role": user.role})
    return TokenResponse(access_token=token, role=user.role, organization=org.name)

@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest, db: Any = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == req.email))
    user = result.scalars().first()
    if not user or not verify_password(req.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token({"sub": user.id, "org_id": user.organization_id, "role": user.role})
    return TokenResponse(access_token=token, role=user.role, organization="Enterprise")

@router.get("/me")
async def get_me(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role,
        "organization_id": user.organization_id
    }

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.dependencies.auth import get_current_user

from api.dependencies.database import get_db
from api.schemas.auth import RegisterRequest, LoginRequest

from models.user import User
from repositories.user_repository import UserRepository
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):

    existing_user = UserRepository.find_by_email(db, request.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    user = User(
        name=request.name,
        email=request.email,
        password_hash=AuthService.hash_password(request.password),
    )

    UserRepository.create(db, user)

    return {"message": "User created successfully"}


@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = UserRepository.find_by_email(db, request.email)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not AuthService.verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = AuthService.create_access_token(user.id)

    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
    }

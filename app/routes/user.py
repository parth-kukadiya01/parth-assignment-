from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.schemas import UserCreate, UserRead, Token, UserLogin
from app.models.models import User
from app.utils.dependencies import get_current_user, require_admin
from app.logics.user import register_new_user, login_user, get_all_users_logic

router = APIRouter()

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(user_data: UserCreate):
    user = register_new_user(user_data)
    if user is None:
        raise HTTPException(status_code=400, detail="Username already registered")
    return user


@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin):
    token = login_user(user_credentials)
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return token


@router.get("/me", response_model=UserRead)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/", response_model=list[UserRead])
def get_all_users(current_user: User = Depends(require_admin)):
    return get_all_users_logic()
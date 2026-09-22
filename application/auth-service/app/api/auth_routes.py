from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.schemas.user import UserRegister
from app.schemas.login import LoginRequest

from app.core.database import get_db

from app.repositories.user_repository import UserRepository

from app.core.security import (
    verify_password,
    create_access_token
)

from app.middleware.auth_middleware import get_current_user

router = APIRouter()


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    created_user = UserRepository.create_user(
        db=db,
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        role=user.role
    )

    return {
        "id": created_user.id,
        "full_name": created_user.full_name,
        "email": created_user.email,
        "role": created_user.role
    }


@router.post("/login")
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):

    existing_user = UserRepository.get_by_email(
        db,
        user.email
    )

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        existing_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "user_id": existing_user.id,
            "sub": existing_user.email,
            "role": existing_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me")
def get_me(
    current_user: dict = Depends(get_current_user)
):
    return {
        "message": "Authorized",
        "user": current_user
    }


# NEW ROUTE
@router.get("/recruiter-dashboard")
def recruiter_dashboard(
    current_user: dict = Depends(get_current_user)
):

    if current_user["role"] != "recruiter":
        raise HTTPException(
            status_code=403,
            detail="Recruiter Only"
        )

    return {
        "message": "Welcome Recruiter",
        "user": current_user
    }
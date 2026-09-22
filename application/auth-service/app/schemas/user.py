from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str = "candidate"


class UserLogin(BaseModel):
    email: EmailStr
    password: str
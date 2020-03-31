from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: Optional[str] = None


class UserBaseInDB(UserBase):
    id: int = None

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class UserCreate(UserBaseInDB):
    email: str
    password: str


class OpenUserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class OpenUserUpdate(BaseModel):
    email: EmailStr = None
    username: str = None
    password: str = None


# Additional properties to return via API
class User(UserBaseInDB):
    pass


# Additional properties stored in DB
class UserInDB(UserBaseInDB):
    hashed_password: str

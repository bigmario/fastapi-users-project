from datetime import date
from typing import Optional

from fastapi_users import models


class User(models.BaseUser):
    first_name: str
    last_name: str
    birth_date: date
    role: str
    phone: str
    address: str


class UserCreate(models.BaseUserCreate):
    first_name: str
    last_name: str
    birth_date: date
    role: str
    phone: str
    address: str


class UserUpdate(models.BaseUserUpdate):
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: date
    role: str
    phone: str
    address: str


class UserDB(User, models.BaseUserDB):
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: date
    role: str
    phone: str
    address: str

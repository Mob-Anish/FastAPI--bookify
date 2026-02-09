from datetime import datetime
from pydantic import BaseModel, Field
import uuid


class UserModel(BaseModel):
    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool
    password_hash: str = Field(exclude=True)
    created_at: datetime
    updated_at: datetime


class UserCreateModel(BaseModel):
    username: str = Field(max_length=18)
    email: str = Field(max_length=40)
    password: str = Field(max_length=12)

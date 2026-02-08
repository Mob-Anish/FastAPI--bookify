from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    first_name: str = Field(max_length=6)
    last_name: str = Field(max_length=8)


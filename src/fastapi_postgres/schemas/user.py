from pydantic import BaseModel


class UserBase(BaseModel):
    id: int


class UserInformation(UserBase):
    height: float

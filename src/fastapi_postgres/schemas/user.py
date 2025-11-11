from typing import List
from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    height: float
    eyesight: List[float]

    class Config:
        orm_mode = True


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    height: float
    eyesight: List[float]

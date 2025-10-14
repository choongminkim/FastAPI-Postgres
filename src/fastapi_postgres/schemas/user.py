from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    height: float

    class Config:
        orm_mode = True

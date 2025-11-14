from pydantic import BaseModel


class MathBase(BaseModel):
    x: float


class MathOutput(BaseModel):
    result: float

# from sqlalchemy import Column, Integer, Float
from typing import List
from ..database import Base
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column

from pydantic import BaseModel, ConfigDict


class UserModel(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    height: Mapped[float] = mapped_column()
    eyesight: Mapped[List[float]] = mapped_column(JSON, nullable=True)

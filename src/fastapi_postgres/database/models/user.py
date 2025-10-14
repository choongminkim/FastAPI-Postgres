# from sqlalchemy import Column, Integer, Float
from ..database import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    height: Mapped[float] = mapped_column()

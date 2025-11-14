from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_postgres.database.models.user import UserModel, UserCreate, UserRead


def create_user(db: AsyncSession, user: UserCreate) -> UserModel:
    db_user = UserModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def read_user(db: AsyncSession, user_id: int) -> Optional[UserModel]:
    query = select(UserModel).where(UserModel.id == user_id)
    result = db.execute(query)

    return result.scalar_one_or_none()

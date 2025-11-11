from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_postgres.database.models.user import UserModel, UserCreate, UserRead


async def create_user(db: AsyncSession, user: UserCreate) -> UserModel:
    db_user = UserModel(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def read_user(db: AsyncSession, user_id: int) -> Optional[UserModel]:
    query = select(UserModel).where(UserModel.id == user_id)
    result = await db.execute(query)

    return result.scalar_one_or_none()

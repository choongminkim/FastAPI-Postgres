from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi_postgres.schemas import user as sch_user
from fastapi_postgres.database.models import user as db_user


class UserService:
    @staticmethod
    async def create_user(user_info: sch_user.UserBase, db: AsyncSession):
        result = await db.execute(
            select(db_user.User).where(db_user.User.id == user_info.id)
        )

        if result.scalar_one_or_none():
            raise Exception(f"user_id: {user_info.id} already in user")

        user = db_user.User(**user_info.model_dump())
        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user

    @staticmethod
    async def check_user(user_id: int, db: AsyncSession):
        result = await db.execute(
            select(db_user.User).where(db_user.User.id == user_id)
        )
        user = result.scalar_one_or_none()

        if not user:
            raise Exception(f"user_id: {user_id} is not found")
        return user

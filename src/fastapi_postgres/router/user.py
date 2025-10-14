from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_postgres.schemas import user as sch_user
from fastapi_postgres.database.models import user as db_user
from fastapi_postgres.database.database import get_async_db

user_router = APIRouter(prefix="/user", tags=["user"])


class UserAlreadyExists(Exception): ...


@user_router.post("/create")
async def creat_user(
    info: sch_user.UserInformation, db: AsyncSession = Depends(get_async_db)
):

    result = await db.execute(select(db_user.User).where(db_user.User.id == info.id))

    if result.scalar_one_or_none():
        raise UserAlreadyExists("id already in use")

    user = db_user.User(**info.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)


@user_router.get("/get")
async def get_user(id: sch_user.UserBase):
    pass

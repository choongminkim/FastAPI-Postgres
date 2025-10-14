from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_postgres.services.user import UserService
from fastapi_postgres.schemas import user as sch_user
from fastapi_postgres.database.models import user as db_user
from fastapi_postgres.database.database import get_async_db

user_router = APIRouter(prefix="/user", tags=["user"])


# class UserAlreadyExists(Exception): ...


@user_router.post("/create")
async def creat_user(
    user_info: sch_user.UserBase, db: AsyncSession = Depends(get_async_db)
):
    try:
        user = await UserService.create_user(user_info=user_info, db=db)
        # return user
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))


@user_router.get("/check", response_model=sch_user.UserBase)
async def check_user(user_id: int, db: AsyncSession = Depends(get_async_db)):
    try:
        user = await UserService.check_user(user_id=user_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

    return user

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_postgres.crud import user as crud_user
from fastapi_postgres.schemas import user as sch_user
from fastapi_postgres.database.models import user as db_user
from fastapi_postgres.database.database import get_async_db

router = APIRouter(prefix="/user", tags=["user"])


# class UserAlreadyExists(Exception): ...


@router.post("/create")
async def creat_user(
    user: sch_user.UserCreate, db: AsyncSession = Depends(get_async_db)
):
    try:
        user = await crud_user.create_user(db=db, user=user)
        return user
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/read")
async def read_user(user_id: int, db: AsyncSession = Depends(get_async_db)):
    try:
        user = await crud_user.read_user(db=db, user_id=user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return user


# @router.get("/check", response_model=sch_user.UserBase)
# async def check_user(user_id: int, db: AsyncSession = Depends(get_async_db)):
#     try:
#         user = await UserService.check_user(user_id=user_id, db=db)

#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))

#     return user

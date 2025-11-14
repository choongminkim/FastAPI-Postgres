from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_postgres.crud import user as crud_user
from fastapi_postgres.database.models.user import *
from fastapi_postgres.database.database import get_db

router = APIRouter(prefix="/user", tags=["user"])


# class UserAlreadyExists(Exception): ...


@router.post("/create")
def creat_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        user = crud_user.create_user(db=db, user=user)
        return user
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.get("/read")
def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    try:
        user = crud_user.read_user(db=db, user_id=user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return user

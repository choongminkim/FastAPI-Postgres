from fastapi import APIRouter

from fastapi_postgres.schemas.math import *
from fastapi_postgres.exceptions.math import *

router = APIRouter(prefix="/math", tags=["math"])


@router.post("/multiplication")
async def multiply(args: MathMultiplication):
    try:
        return args.x * args.y

    except Exception as e:
        raise MultiplicationError("곱셈이 안됨")

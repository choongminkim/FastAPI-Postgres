import json

from fastapi import APIRouter, Depends, status, Request
from fastapi.responses import JSONResponse

from fastapi_postgres.api.deps import get_math_service
from fastapi_postgres.schemas.math import MathBase, MathOutput
from fastapi_postgres.services.math import MathService
from fastapi_postgres.services.utils import set_sha256_hash

router = APIRouter(prefix="/math", tags=["math"])


def get_redis(request: Request):
    return request.app.state.redis


@router.post("/multiplication", response_model=MathOutput)
def add_number(
    args: MathBase,
    service: MathService = Depends(get_math_service),
    redis=Depends(get_redis),
):
    key = set_sha256_hash(f"{args.x}")
    try:
        redis_value = redis.get(key)
        if redis_value is None:
            result = service.do_add(args.x)
            redis.set(key, result, ttl=60)
        else:
            result = float(redis_value)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"result": result},
        )

    except Exception as e:
        raise e


@router.get("/test")
def test_cache():
    return "asdf"

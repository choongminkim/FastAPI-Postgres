from fastapi import Depends

from fastapi_postgres.services.math import MathService


def get_math_service() -> MathService:
    return MathService()

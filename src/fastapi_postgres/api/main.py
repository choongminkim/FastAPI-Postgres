from fastapi import APIRouter

from fastapi_postgres.api.routers import user, image, math, registration

api_router = APIRouter()

api_router.include_router(image.router)
api_router.include_router(math.router)
api_router.include_router(user.router)
api_router.include_router(registration.router)

import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from fastapi_postgres.exceptions.handler import *
from fastapi_postgres.api.main import api_router
from fastapi_postgres.database.database import init_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

    await close_db()


def create_app():
    app = FastAPI(lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router=api_router)

    set_error_handlers(app)

    return app


app = create_app()


if __name__ == "__main__":
    pass

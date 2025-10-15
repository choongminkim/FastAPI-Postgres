import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from fastapi_postgres.router.user import user_router
from fastapi_postgres.database.database import init_db, close_db


@asynccontextmanager
async def lifespan(router: APIRouter):
    await init_db()
    yield

    await close_db()


def creat_app():
    app = FastAPI(lifespan=lifespan)
    # app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router=user_router)
    return app


app = creat_app()

if __name__ == "__main__":
    pass

import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from fastapi_postgres.router.user import user_router
from fastapi_postgres.database.database import Base, async_engine


@asynccontextmanager
async def lifespan(router: APIRouter):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all, checkfirst=True)
    yield


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

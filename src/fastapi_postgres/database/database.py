from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


async_engine = None
async_session_maker = None


async def init_db():
    try:
        global async_engine, async_session_maker

        async_engine = create_async_engine(
            "postgresql+asyncpg://postgres@localhost:11001/postgres", echo=True
        )

        async_session_maker = async_sessionmaker(
            bind=async_engine, expire_on_commit=False
        )

        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all, checkfirst=True)

    except Exception as e:
        print(f"\033[31mERROR\033[0m: Database initialization failed: {e}")
        raise


async def close_db():
    global async_engine
    if async_engine:
        await async_engine.dispose()


async def get_async_db():
    async with async_session_maker() as session:
        yield session

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

async_engine = create_async_engine(
    "postgresql+asyncpg://postgres@localhost:11001/postgres", echo=True
)


async_session_maker = async_sessionmaker(bind=async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_db():
    async with async_session_maker() as session:
        yield session

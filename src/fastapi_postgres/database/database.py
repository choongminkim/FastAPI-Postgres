from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class Base(DeclarativeBase):
    pass


engine = None
session_maker = None


def init_db():
    try:
        global engine, session_maker
        engine = create_engine(
            "postgresql+psycopg2://postgres@localhost:11001/postgres"
        )

        session_maker = sessionmaker(bind=engine, expire_on_commit=False)
        with engine.begin() as conn:
            Base.metadata.create_all(bind=conn, checkfirst=True)

    except Exception as e:
        print(f"\033[31mERROR\033[0m: Database initialization failed: {e}")
        raise


def close_db():
    global engine
    if engine:
        engine.dispose()


def get_db() -> Generator[Session, None, None]:
    session = session_maker()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config.settings import settings


SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}'
    f'@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_NAME}'
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session

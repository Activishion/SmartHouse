import uvicorn

from logging import getLogger, StreamHandler, Formatter, INFO, ERROR, LogRecord
from logging.handlers import RotatingFileHandler

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_users import FastAPIUsers
from redis import asyncio as aioredis

from config.settings import settings
from location.routers import router as location_router
from sensors.routers import router as sensor_router
from users.auth import auth_backend
from users.manager import get_user_manager
from users.models import User
from users.schemas import UserRead, UserCreate, UserUpdate


# APP
def create_app() -> FastAPI:
    """
    The application factory using FastAPI framework.
    """

    app = FastAPI(
        title = settings.TITLE_APP,
        version = settings.VERSION_APP,
        debug = settings.DEBUG,
        docs_url = "/docs",
        openapi_url ='/api/openapi.json',
        default_response_class = ORJSONResponse,
        redoc_url = None
    )

    origins_host: list = [
        'http://localhost:3000',
        'http://localhost:8000'
    ]

    init_routers(app)
    init_middleware(app, origins_host)
    setup_exception_handlers(app)
    return app


def init_routers(app: FastAPI) -> None:
    app.include_router(location_router, prefix="/api/v1/locations", tags=['Locations'])
    app.include_router(sensor_router, prefix="/api/v1/sensors", tags=['Sensors'])
    app.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix="/auth/jwt",
        tags=["Auth"]
    )
    app.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix="/auth",
        tags=["Auth"]
    )
    app.include_router(
        fastapi_users.get_verify_router(UserRead),
        prefix="/auth",
        tags=["Auth"]
    )
    app.include_router(
        fastapi_users.get_reset_password_router(),
        prefix="/auth",
        tags=["Auth"]
    )
    app.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
        prefix="/users",
        tags=["Users"]
    )

def init_middleware(app: FastAPI, origins_host: list) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins_host,
        allow_credentials=False,
        allow_methods=['OPTIONS', 'HEAD', 'GET', 'POST', 'PUT', 'DELETE'],
        allow_headers=[
            'Content-Type',
            'Set-Cookie',
            'Access-Control-Allow-Headers',
            'Access-Control-Allow-Credentials',
            'Access-Control-Allow-Origin'
        ]
    )

def setup_exception_handlers(app: FastAPI) -> None:
    pass
    # app.add_exception_handler(
    #     UserEmailAlreadyExistsError,
    #     user_email_already_exists_error_handler,
    # )


# Users
fastapi_users = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)


# Logging
def init_logger(name):
    logger = getLogger(name)
    FORMAT = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'
    logger.setLevel(INFO)

    sh = StreamHandler()
    sh.setFormatter(Formatter(FORMAT))
    sh.setLevel(ERROR)
    sh.addFilter(logger_filter)

    # fh = RotatingFileHandler(
    #     filename='logs/app.log',
    #     maxBytes=5000000,
    #     backupCount=10
    # )
    # fh.setFormatter(Formatter(FORMAT))
    # fh.setLevel(INFO)
    # fh.addFilter(logger_filter)

    logger.addHandler(sh)
    # logger.addHandler(fh)


def logger_filter(log: LogRecord) -> int:
    if 'password' in str(log.msg):
        return 0
    return 1

init_logger('app')
logger = getLogger('app.main')


# @create_app.on_event('startup')
# async def startup_event():
#     redis = aioredis.from_url('redis://localhost', encoding='utf-8', decode_responses=True)
#     FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')


if __name__ == '__main__':
    uvicorn.run(
        'main:create_app',
        port = 8000,
        host = settings.HOST,
        reload = settings.RELOAD,
        factory = True
    )

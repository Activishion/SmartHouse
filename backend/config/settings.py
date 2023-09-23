from starlette.config import Config


config = Config('../.env')

class Settings:
    """ Main app """
    TITLE_APP: str = config('TITLE_APP')
    VERSION_APP: str = config('VERSION_APP')

    DEBUG: bool = config('DEBUG')
    SECRET_KEY: str = config('SECRET_KEY')

    """ DB """
    POSTGRES_NAME: str = config('POSTGRES_NAME')
    POSTGRES_USER: str = config('POSTGRES_USER')
    POSTGRES_PASSWORD: str = config('POSTGRES_PASSWORD')
    POSTGRES_HOST: str = config('POSTGRES_HOST')
    POSTGRES_PORT: str = config('POSTGRES_PORT')

    """ Deploy """
    PORT: str = config('PORT')
    HOST: str = config('HOST')
    RELOAD: bool = config('RELOAD')


settings = Settings()

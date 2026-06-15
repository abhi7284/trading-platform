from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str

    database_url: str

    redis_host: str
    redis_port: int

    jwt_secret: str
    # jwt_algorithm: str
    jwt_algorithm: str = "HS256"

    upstox_api_key: str
    upstox_api_secret: str

    class Config:
        env_file = ".env"


settings = Settings()

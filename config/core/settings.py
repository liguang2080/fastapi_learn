import os

from anyio.functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str
    debug: bool = False
    database_url: str
    database_password: SecretStr

    secret_key: SecretStr
    api_key: SecretStr

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


# 根据环境加载.env.dev .env.prod .env.test
def get_fastapi_env() -> str:
    return os.getenv("FASTAPI_ENV", "dev")


# 函数用相同参数调用时，直接返回上一次的结果，不再重新执行函数。
@lru_cache()
def get_settings() -> Settings:
    env = get_fastapi_env()
    return Settings(environment=env, _env_file=f".env.{env}")

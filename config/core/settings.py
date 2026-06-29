from anyio.functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    database_url: str
    database_password: SecretStr

    secret_key: SecretStr
    api_key: SecretStr

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }


@lru_cache()  # 函数用相同参数调用时，直接返回上一次的结果，不再重新执行函数。
def get_settings() -> Settings:
    return Settings()

# 全局校验
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

get_bearer_token = HTTPBearer(auto_error=False)


async def verify_token(credentials: Annotated[HTTPAuthorizationCredentials, Depends(get_bearer_token)]):
    print("校验token")
    print(f"当前Token: {credentials}")

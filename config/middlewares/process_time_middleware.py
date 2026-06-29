from time import perf_counter

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_name: str = "X-Process-Time"):
        super().__init__(app)
        self.header_name = header_name

    async def dispatch(self, request: Request, call_next):
        start = perf_counter()

        response = await call_next(request)

        cost = perf_counter() - start
        response.headers[self.header_name] = f"{cost:.6f}"

        return response

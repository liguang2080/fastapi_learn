import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from app.api import demo
from config.core.exception_handlers import register_exception_handlers
from config.dependencies.auth import verify_token
from config.middlewares.process_time_middleware import ProcessTimeMiddleware


async def init_database():
    await asyncio.sleep(0.1)
    print("数据库初始化完成")


async def close_database():
    await asyncio.sleep(0.1)
    print("数据库关闭完成")


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("应用启动中")
    await init_database()

    yield

    print("应用关闭中")
    await close_database()


app = FastAPI(
    title="商品管理API",
    description="一个完整的FASTAPI示例应用",
    version="1.0.0",
    lifespan=lifespan,
    dependencies=[
        Depends(verify_token)
    ]
)

app.add_middleware(ProcessTimeMiddleware, header_name="X-Cost-Time")

app.include_router(demo.router, prefix="/api/demo", tags=["测试"])

# 注册异常处理器
register_exception_handlers(app)

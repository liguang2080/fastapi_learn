from fastapi import FastAPI
from config.core.exception_handlers import register_exception_handlers
from app.api import demo

app = FastAPI(
    title="商品管理API",
    description="一个完整的FASTAPI示例应用",
    version="1.0.0",
)

app.include_router(demo.router, prefix="/api/demo", tags=["测试"])

# 注册异常处理器
register_exception_handlers(app)

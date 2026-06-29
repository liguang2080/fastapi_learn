from fastapi import APIRouter, HTTPException
from app.schema.demo import Item

router = APIRouter()


# 模拟数据库：用字典存储商品数据
items_db = {}


@router.get("")
async def read_root():
    return {"Hello": "World"}


# 参数类型会自动校验
@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="商品不存在")

    return {"item_id": item_id, "q": q, **items_db[item_id]}


# 自动校验模型的参数
@router.post("/items")
def create_item(item: Item):
    item_id = len(items_db) + 1

    # model_dump() 将 Pydantic 模型转为普通字典（v2 API)
    items_db[item_id] = item.model_dump()

    return {"item_id": item_id, **items_db[item_id]}


@router.get("/items")
def read_items(skip: int = 0, limit: int = 10):
    # return {"skip": skip, "limit": limit}
    return items_db

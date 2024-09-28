from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items: List[Item] = []

# @app.post("/items/")
# async def create_item(item: Item):
#     items.append(item)
#     return {"item": item}

# @app.get("/items/")
# async def read_items():
#     return items

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

@app.get("/")
async def root():
    return {"message": "Hello World"}

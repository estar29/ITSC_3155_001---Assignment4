# Evan Stark - October 17th 2024 - ITSC 3155 001
# This program simulates a very basic FastAPI application.

# Import all needed packages.
from typing import Union
from fastapi import FastAPI
# Pydantic to declare body for a put request.
from pydantic import BaseModel

# Creating the app.
app = FastAPI()

# Creating class
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

# Basic get path that prints Hello World message.
@app.get("/")
def read_root():
    return{"Hello": "World"}

# get path that prints item id and a custom string.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# put method to update an item.
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
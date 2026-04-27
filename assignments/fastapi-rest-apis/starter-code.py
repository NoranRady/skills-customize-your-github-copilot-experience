from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the Item model
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage for items
items: List[Item] = []

# TODO: Implement the endpoints here
# - GET /items
# - POST /items
# - PUT /items/{item_id}
# - DELETE /items/{item_id}

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}
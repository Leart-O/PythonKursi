from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/item")
def read_item():
    return {"item": ["item1", "item2", "item3"]}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
def create_item(item: str, price: float):
    return {"item": item, "price": price}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: str, price: float):
    return {"item_id": item_id, "item": item, "price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
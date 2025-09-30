from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Hello, World!"}

@app.get("/greet")

def greet(name: str):
    return {"message": f"Hello, {name}!"}
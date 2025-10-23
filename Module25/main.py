from fastapi import FastAPI
from typing import List
import database
import models
from models import Movie, MovieCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to CRUD"}
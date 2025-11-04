from fastapi import FastAPI, HTTPException
from typing import List
import database
import models
from models import Student, StudentCreate

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to CRUD"}


@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate):
    """Create a new student entry in the database."""
    sid = database.create_student(student)
    return models.Student(id=sid, **student.model_dump())


@app.get("/students/", response_model=List[Student])
def read_students():
    """Return all students"""
    return database.read_students()


@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    """Read a single student"""
    student = database.read_student(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate):
    """Update student"""
    updated = database.update_student(student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return models.Student(id=student_id, **student.model_dump())


@app.delete("/students/{student_id}", response_model=dict)
def delete_student(student_id: int):
    """Delete student"""
    deleted = database.delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

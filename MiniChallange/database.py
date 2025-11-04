import sqlite3
import re
from typing import Optional, List
from models import Student, StudentCreate

DB_FILE = "students.db"
BEHAVIOUR_ALLOWED = (1, 3, 5)
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def create_connection():
    """Creates a connection to the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    """Creates the students table in the database."""
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            grade INTEGER NOT NULL,
            avg_grade REAL,
            email TEXT,
            behaviour INTEGER NOT NULL CHECK (behaviour IN (1,3,5))
        )
        """
    )
    conn.commit()
    conn.close()


create_table()


def _validate_email(email: Optional[str]) -> bool:
    if email is None or email == "":
        return True
    return bool(EMAIL_RE.match(email))


def _validate_behaviour(b: int) -> bool:
    return b in BEHAVIOUR_ALLOWED


def create_student(student: StudentCreate) -> int:
    """
    Adds a new student to the database. Returns the new student's id.
    """
    if not _validate_email(getattr(student, "email", None)):
        raise ValueError("invalid email")
    if not _validate_behaviour(getattr(student, "behaviour", 0)):
        raise ValueError(f"behaviour must be one of {BEHAVIOUR_ALLOWED}")

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (first_name, last_name, grade, avg_grade, email, behaviour) VALUES (?, ?, ?, ?, ?, ?)",
        (
            student.first_name,
            student.last_name,
            student.grade,
            getattr(student, "avg_grade", None),
            getattr(student, "email", None),
            student.behaviour,
        ),
    )
    conn.commit()
    sid = cur.lastrowid
    conn.close()
    return sid


def read_students() -> List[Student]:
    """
    Retrieves all students from the database.
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY last_name, first_name")
    rows = cur.fetchall()
    students = [
        Student(
            id=row["id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            grade=row["grade"],
            avg_grade=row["avg_grade"],
            email=row["email"],
            behaviour=row["behaviour"],
        )
        for row in rows
    ]
    conn.close()
    return students


def read_student(student_id: int) -> Optional[Student]:
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cur.fetchone()
    conn.close()
    if row is None:
        return None
    return Student(
        id=row["id"],
        first_name=row["first_name"],
        last_name=row["last_name"],
        grade=row["grade"],
        avg_grade=row["avg_grade"],
        email=row["email"],
        behaviour=row["behaviour"],
    )


def update_student(student_id: int, student: StudentCreate) -> bool:
    """
    Updates an existing student. Returns True if a row was updated.
    """
    if not _validate_email(getattr(student, "email", None)):
        raise ValueError("invalid email")
    if not _validate_behaviour(getattr(student, "behaviour", 0)):
        raise ValueError(f"behaviour must be one of {BEHAVIOUR_ALLOWED}")

    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET first_name = ?, last_name = ?, grade = ?, avg_grade = ?, email = ?, behaviour = ? WHERE id = ?",
        (
            student.first_name,
            student.last_name,
            student.grade,
            getattr(student, "avg_grade", None),
            getattr(student, "email", None),
            student.behaviour,
            student_id,
        ),
    )
    conn.commit()
    updated = cur.rowcount
    conn.close()
    return updated > 0


def delete_student(student_id: int) -> bool:
    """
    Deletes a student from the database. Returns True if deleted.
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    deleted = cur.rowcount
    conn.close()
    return deleted > 0

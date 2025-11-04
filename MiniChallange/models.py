import re
from typing import Optional
from pydantic import BaseModel, field_validator

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    grade: int
    avg_grade: Optional[float] = None
    email: Optional[str] = None
    behaviour: int

    @field_validator("email")
    def validate_email(cls, v: Optional[str]) -> Optional[str]:
        if v is None or v == "":
            return None
        if not EMAIL_RE.match(v):
            raise ValueError("invalid email")
        return v

    @field_validator("behaviour")
    def validate_behaviour(cls, v: int) -> int:
        if v not in (1, 3, 5):
            raise ValueError("behaviour must be one of (1, 3, 5)")
        return v


class Student(StudentCreate):
    id: int

    model_config = {"from_attributes": True}
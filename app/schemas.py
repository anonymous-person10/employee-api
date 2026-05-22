from pydantic import BaseModel
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str
    role: str
    email: Optional[str] = None


class EmployeeCreate(BaseModel):
    name: str
    role: str
    email: Optional[str] = None


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    email: Optional[str] = None

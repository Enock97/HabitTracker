from pydantic import BaseModel
from typing import Optional

print("✅ backend/app/models.py loaded") 

class Habit(BaseModel):
    id: str
    name: str
    completed: bool

class HabitCreate(BaseModel):
    name: str

class HabitUpdate(BaseModel):
    name: Optional[str] = None
    completed: Optional[bool] = None

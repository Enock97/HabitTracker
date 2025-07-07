print("🆗 Habit model present in bundle")

from pydantic import BaseModel
from typing import Optional

class Habit(BaseModel):
    id: str
    name: str
    completed: bool

class HabitCreate(BaseModel):
    name: str

class HabitUpdate(BaseModel):
    name: Optional[str] = None
    completed: Optional[bool] = None

from pydantic import BaseModel
from typing import Optional

class HabitCreate(BaseModel):
    name: str

class HabitUpdate(BaseModel):
    name: Optional[str] = None
    completed: Optional[bool] = None

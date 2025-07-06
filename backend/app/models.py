from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Habit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    created_at: date = Field(default_factory=date.today)
    completed: bool = False

class HabitCreate(SQLModel):
    name: str

class HabitUpdate(SQLModel):
    name: Optional[str] = None
    completed: Optional[bool] = None
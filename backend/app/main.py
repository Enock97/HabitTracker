from fastapi import FastAPI, HTTPException
from .database import init_db
from . import crud
from .models import HabitCreate, HabitUpdate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/habits")
def read_habits():
    return crud.get_habits()

@app.get("/habits/{habit_id}")
def read_habit(habit_id: int):
    habit = crud.get_habit(habit_id)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

@app.post("/habits", status_code=201)
def create_habit(habit: HabitCreate):
    return crud.create_habit(habit)

@app.put("/habits/{habit_id}")
def update_habit(habit_id: int, habit: HabitUpdate):
    updated = crud.update_habit(habit_id, habit)
    if updated is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return updated

@app.delete("/habits/{habit_id}")
def delete_habit(habit_id: int):
    deleted = crud.delete_habit(habit_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"detail": "Habit deleted"}
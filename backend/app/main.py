from fastapi import FastAPI, HTTPException
from . import crud
from .models import HabitCreate, HabitUpdate
from mangum import Mangum
from fastapi.responses import Response


app = FastAPI()

handler = Mangum(app)

@app.options("/habits")
def options_habits():
    return Response(status_code=200)

@app.options("/habits/{habit_id}")
def options_habit_id(habit_id: str):
    return Response(status_code=200)

@app.get("/habits")
def read_habits():
    return crud.get_habits()

@app.get("/habits/{habit_id}")
def read_habit(habit_id: str):
    habit = crud.get_habit(habit_id)
    if habit is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

@app.post("/habits", status_code=201)
def create_habit(habit: HabitCreate):
    return crud.create_habit(habit)

@app.put("/habits/{habit_id}")
def update_habit(habit_id: str, habit: HabitUpdate):
    updated = crud.update_habit(habit_id, habit)
    if updated is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return updated

@app.delete("/habits/{habit_id}")
def delete_habit(habit_id: str):
    deleted = crud.delete_habit(habit_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"detail": "Habit deleted"}

@app.get("/")
def root():
    return {"msg": "Habit Tracker backend is live"}
from fastapi import FastAPI, HTTPException
from . import crud
from .models import HabitCreate, HabitUpdate, Habit
from mangum import Mangum
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",                      # local dev
    "https://habit-tracker-two-virid.vercel.app", # prod site
]

app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],       # GET, POST, PUT, DELETE, OPTIONS …
     allow_headers=["*"],       # Accept, Content-Type, Authorization …
)

handler = Mangum(app)

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

@app.put("/habits/{habit_id}", response_model=Habit)
def update_habit(habit_id: str, habit: HabitUpdate):
    return crud.update_habit(habit_id, habit)

@app.delete("/habits/{habit_id}")
def delete_habit(habit_id: str):
    deleted = crud.delete_habit(habit_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"detail": "Habit deleted"}

@app.get("/")
def root():
    return {"msg": "Habit Tracker backend is live"}
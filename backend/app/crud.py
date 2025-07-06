from sqlmodel import Session, select
from .models import Habit, HabitCreate, HabitUpdate
from .database import engine

def get_habits():
    with Session(engine) as session:
        return session.exec(select(Habit)).all()

def get_habit(habit_id: int):
    with Session(engine) as session:
        return session.get(Habit, habit_id)

def create_habit(habit_data: HabitCreate):
    habit = Habit(name=habit_data.name)
    with Session(engine) as session:
        session.add(habit)
        session.commit()
        session.refresh(habit)
        return habit

def update_habit(habit_id: int, habit_data: HabitUpdate):
    with Session(engine) as session:
        habit = session.get(Habit, habit_id)
        if not habit:
            return None
        habit_data_dict = habit_data.dict(exclude_unset=True)
        for key, value in habit_data_dict.items():
            setattr(habit, key, value)
        session.add(habit)
        session.commit()
        session.refresh(habit)
        return habit

def delete_habit(habit_id: int):
    with Session(engine) as session:
        habit = session.get(Habit, habit_id)
        if not habit:
            return None
        session.delete(habit)
        session.commit()
        return habit
from sqlmodel import create_engine

sqlite_url = "sqlite:///habits.db"
engine = create_engine(sqlite_url, echo=False)
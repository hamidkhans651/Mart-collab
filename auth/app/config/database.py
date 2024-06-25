from fastapi import FastAPI
from sqlmodel import SQLModel, Session, create_engine
from contextlib import asynccontextmanager
from app.config.setting import DATABASE_URL

connection_str = str(DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_str)

def get_session():
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creating table")
    SQLModel.metadata.create_all(engine)
    print("table created")
    yield
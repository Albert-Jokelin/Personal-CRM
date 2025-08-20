import time
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from .database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    attempts = 10
    while attempts > 0:
        try:
            create_db_and_tables()
            print("Database connection and table creation successful.")
            break
        except OperationalError:
            print("Database connection failed. Retrying in 5 seconds...")
            attempts -= 1
            time.sleep(5)
    if attempts == 0:
        print("Could not connect to the database after multiple attempts.")


@app.get("/health")
async def read_root():
    return {"status": "ok"}

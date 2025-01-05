from fastapi import FastAPI
from routers import task, user

app = FastAPI()
app.include_router(task.router)
app.include_router(user.router)


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# python -m uvicorn main:app


# Создание таблиц
# from models.user import User
# from backend.db import Base, engine
#
# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)

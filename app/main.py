from fastapi import FastAPI
from routers import users

app = FastAPI()

app.include_router(users)

@app.get("/")
def default():
    return {"data": "Financial Management API is running"}
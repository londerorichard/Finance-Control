from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users, categories, transactions


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(categories.router)
app.include_router(transactions.router)


@app.get("/")
def default():
    return {"data": "Financial Management API is running"}
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users, categories, transactions, auth


app = FastAPI()


# Static files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# Jinja2
templates = Jinja2Templates(directory="app/templates")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
# app.include_router(users.router)
app.include_router(categories.router)
app.include_router(transactions.router)
app.include_router(auth.router)


# API default endpoint
@app.get("/api")
def default():
    return {"data": "Financial Management API is running"}


# Dashboard page
@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )


# Expenses page
@app.get("/expenses")
async def expenses(request: Request):
    return templates.TemplateResponse(
        "expenses.html",
        {"request": request}
    )
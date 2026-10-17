from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from app.auth.dependency import get_current_user

from app.routers import users, categories, transactions, auth


app = FastAPI()


BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)

app.mount(
    "/app/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


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
app.include_router(users.router)


@app.get("/base")
async def base(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="base.html"
    )


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/login.html"
    )


@app.get("/register")
async def register(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth/register.html"
    )


@app.get("/dashboard")
async def dashboard(
    request: Request,
    current_user=Depends(get_current_user)
):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )


@app.get("/categories")
async def categories(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="categories.html"
    )
    
@app.get("/category")
async def category(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="category.html"
    )

@app.get("/news")
async def news(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="news.html"
    )




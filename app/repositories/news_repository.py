import os
from pathlib import Path

from dotenv import load_dotenv
import httpx

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

MARKETAUX_API_URL = "https://api.marketaux.com/v1/news/all"
MARKETAUX_API_TOKEN = os.getenv("MARKETAUX_API_TOKEN")


async def get_financial_news(
    limit: int = 3,
    language: str = "en",
):
    if not MARKETAUX_API_TOKEN:
        raise RuntimeError("MARKETAUX_API_TOKEN is not configured.")

    params = {
        "api_token": MARKETAUX_API_TOKEN,
        "language": language,
        "limit": limit,
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(
            MARKETAUX_API_URL,
            params=params,
        )

        response.raise_for_status()

        data = response.json()

    return data.get("data", [])


async def get_news_by_symbol(
    symbol: str,
    limit: int = 3,
):
    if not MARKETAUX_API_TOKEN:
        raise RuntimeError("MARKETAUX_API_TOKEN is not configured.")

    params = {
        "api_token": MARKETAUX_API_TOKEN,
        "symbols": symbol,
        "language": "en",
        "limit": limit,
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(
            MARKETAUX_API_URL,
            params=params,
        )

        response.raise_for_status()

        data = response.json()

    return data.get("data", [])


async def search_financial_news(
    query: str,
    limit: int = 3,
):
    if not MARKETAUX_API_TOKEN:
        raise RuntimeError("MARKETAUX_API_TOKEN is not configured.")

    params = {
        "api_token": MARKETAUX_API_TOKEN,
        "search": query,
        "language": "en",
        "limit": limit,
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(
            MARKETAUX_API_URL,
            params=params,
        )

        response.raise_for_status()

        data = response.json()

    return data.get("data", [])
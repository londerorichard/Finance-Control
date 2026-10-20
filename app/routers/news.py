import httpx

from fastapi import APIRouter, HTTPException, Query

from app.services.news_service import (
    get_financial_news,
    get_news_by_symbol,
    search_financial_news,
)

router = APIRouter(
    prefix="/news",
    tags=["News"],
)


@router.get("/")
async def read_financial_news(
    limit: int = Query(default=3, ge=1, le=3),
):
    try:
        articles = await get_financial_news(limit=limit)

        return {
            "count": len(articles),
            "articles": articles,
        }

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=502,
            detail="The external news provider returned an error.",
        ) from error

    except httpx.RequestError as error:
        raise HTTPException(
            status_code=503,
            detail="The news provider is currently unavailable.",
        ) from error

    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail="News API configuration error.",
        ) from error


@router.get("/symbol/{symbol}")
async def read_news_by_symbol(
    symbol: str,
    limit: int = Query(default=3, ge=1, le=3),
):
    try:
        articles = await get_news_by_symbol(
            symbol=symbol,
            limit=limit,
        )

        return {
            "symbol": symbol.upper(),
            "count": len(articles),
            "articles": articles,
        }

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=502,
            detail="The external news provider returned an error.",
        ) from error

    except httpx.RequestError as error:
        raise HTTPException(
            status_code=503,
            detail="The news provider is currently unavailable.",
        ) from error

    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail="News API configuration error.",
        ) from error


@router.get("/search")
async def search_news(
    query: str = Query(min_length=2, max_length=100),
    limit: int = Query(default=3, ge=1, le=3),
):
    try:
        articles = await search_financial_news(
            query=query,
            limit=limit,
        )

        return {
            "query": query,
            "count": len(articles),
            "articles": articles,
        }

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=502,
            detail="The external news provider returned an error.",
        ) from error

    except httpx.RequestError as error:
        raise HTTPException(
            status_code=503,
            detail="The news provider is currently unavailable.",
        ) from error

    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail="News API configuration error.",
        ) from error
const NEWS_API_URL = "http://127.0.0.1:8000/news/";


export async function getFinancialNews(limit = 3) {
    const url = new URL(NEWS_API_URL);
    url.searchParams.set("limit", limit);

    console.log("Requesting financial news:", url.href);

    const response = await fetch(url);

    console.log("HTTP status:", response.status);

    const responseText = await response.text();

    console.log("Response body:", responseText);

    if (!response.ok) {
        throw new Error("Could not retrieve financial news.");
    }

    return JSON.parse(responseText);
}

export async function searchNewsBySymbol(token, symbol, limit = 3) {
    const normalizedSymbol = symbol.trim().toUpperCase();

    if (!normalizedSymbol) {
        throw new Error("A financial symbol is required.");
    }

    const url = new URL(
        `${NEWS_API_URL}/symbol/${encodeURIComponent(normalizedSymbol)}`
    );

    url.searchParams.set("limit", limit);

    const response = await fetch(url, {
        method: "GET",
        credentials: "include",
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(
            data.detail || "Could not retrieve news for this symbol."
        );
    }

    return data;
}


export async function searchNews(token, query, limit = 3) {
    const normalizedQuery = query.trim();

    if (normalizedQuery.length < 2) {
        throw new Error("The search query must contain at least 2 characters.");
    }

    const url = new URL(`${NEWS_API_URL}/search`);

    url.searchParams.set("query", normalizedQuery);
    url.searchParams.set("limit", limit);

    const response = await fetch(url, {
        method: "GET",
        credentials: "include",
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(
            data.detail || "Could not search financial news."
        );
    }

    return data;
}

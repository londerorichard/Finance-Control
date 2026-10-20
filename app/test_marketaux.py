import os

import httpx
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()

# 2. Retrieve the API token
API_TOKEN = os.getenv("MARKETAUX_API_TOKEN")

if not API_TOKEN:
    raise ValueError("MARKETAUX_API_TOKEN was not found.")

# 3. Configure the request
url = "https://api.marketaux.com/v1/news/all"

params = {
    "api_token": API_TOKEN,
    "language": "en",
    "limit": 3,
}

try:
    # 4. Send the GET request
    response = httpx.get(url, params=params, timeout=15.0)

    # 5. Check the response status
    response.raise_for_status()

    # 6. Parse the JSON response
    data = response.json()

    # 7. Retrieve and count the articles
    articles = data.get("data", [])

    print(f"Articles received: {len(articles)}")

    # 8. Print the first headline
    if articles:
        print("First headline:", articles[0].get("title"))

except httpx.HTTPStatusError as error:
    print(f"API returned HTTP {error.response.status_code}.")
    print("Response:", error.response.text)

except httpx.RequestError as error:
    print(f"Could not connect to Marketaux: {error}")

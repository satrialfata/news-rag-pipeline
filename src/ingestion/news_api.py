import requests

API_KEY = "09be98ef558547ca8ca0cfb86d85a18f"

def fetch_news():
    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"country=us&apiKey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        print("Error:", data)
        return []

    return data.get("articles", [])
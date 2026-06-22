import requests
from bs4 import BeautifulSoup


def extract_article(url):
    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator=" ", strip=True)

        return {
            "content": text
        }

    except Exception as e:
        print(f"Error: {e}")
        return None
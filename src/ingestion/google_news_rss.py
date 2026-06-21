import feedparser


def fetch_news(limit=50):
    rss_url = "https://news.google.com/rss?hl=id&gl=ID&ceid=ID:id"

    feed = feedparser.parse(rss_url)

    articles = []

    for entry in feed.entries[:limit]:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", "")
        })

    return articles
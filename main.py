from src.ingestion.google_news_rss import fetch_news

news = fetch_news()

print(news[:3])
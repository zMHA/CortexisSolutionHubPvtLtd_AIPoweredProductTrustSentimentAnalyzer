import requests
from bs4 import BeautifulSoup

def scrape_reviews(url):
    # For Hugging Face demo: simple static placeholder
    # Real scraping may be blocked by websites' TOS — use APIs in production
    fake_reviews = [
        "This product is great! Works exactly as described.",
        "Average quality, not bad but could be better.",
        "Totally fake product. Waste of money!",
        "Loved it, delivery was quick and packaging was nice.",
        "Stopped working after a week. Disappointed."
    ]
    return fake_reviews

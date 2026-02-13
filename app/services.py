import requests
from bs4 import BeautifulSoup

def analyze_website(url: str):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title else ""

    meta = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta.get("content", "") if meta else ""

    h1 = len(soup.find_all("h1"))
    h2 = len(soup.find_all("h2"))

    images = soup.find_all("img")
    missing_alt = len([img for img in images if not img.get("alt")])

    word_count = len(soup.get_text().split())

    return {
        "title": title,
        "meta_description": meta_desc,
        "h1_count": h1,
        "h2_count": h2,
        "images_without_alt": missing_alt,
        "word_count": word_count
    }

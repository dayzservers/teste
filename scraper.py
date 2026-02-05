import requests
import json
import os
from bs4 import BeautifulSoup

STATE_FILE = "state.json"
BASE_URL = "https://www.bbc.com/portuguese"

state = {"links": []}
if os.path.exists(STATE_FILE):
    state = json.load(open(STATE_FILE))

html = requests.get(BASE_URL, timeout=15).text
soup = BeautifulSoup(html, "html.parser")

articles = []

for a in soup.select("a[href]"):
    href = a["href"]
    if "/portuguese/articles/" in href:
        url = "https://www.bbc.com" + href
        if url in state["links"]:
            continue

        page = requests.get(url, timeout=15).text
        psoup = BeautifulSoup(page, "html.parser")

        title = psoup.find("h1")
        paragraphs = psoup.find_all("p")

        if not title or not paragraphs:
            continue

        summary = " ".join(p.text for p in paragraphs[:3])

        articles.append({
            "title": title.text.strip(),
            "summary": summary.strip(),
            "url": url
        })

        state["links"].append(url)

        if len(articles) >= 5:
            break

json.dump(state, open(STATE_FILE, "w"), indent=2)
json.dump(articles, open("articles.json", "w"), indent=2)

print(f"✔️ {len(articles)} novas notícias coletadas")

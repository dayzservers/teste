import requests
import json
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

STATE_FILE = "state.json"
BASE_URL = "https://www.bbc.com/portuguese"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}

state = {"links": []}
if os.path.exists(STATE_FILE):
    state = json.load(open(STATE_FILE))

resp = requests.get(BASE_URL, headers=HEADERS, timeout=15)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

articles = []

for a in soup.select("a[href]"):
    href = a["href"]

    if "/portuguese/articles/" not in href:
        continue

    url = urljoin("https://www.bbc.com", href)

    if url in state["links"]:
        continue

    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
    except Exception as e:
        print("Erro ao baixar:", url, e)
        continue

    psoup = BeautifulSoup(r.text, "html.parser")

    title = psoup.find("h1")
    paragraphs = psoup.find_all("p")

    if not title or len(paragraphs) < 2:
        continue

    summary = " ".join(p.text.strip() for p in paragraphs[:3])

    articles.append({
        "title": title.text.strip(),
        "summary": summary.strip(),
        "url": url
    })

    state["links"].append(url)

    if len(articles) >= 5:
        break

json.dump(state, open(STATE_FILE, "w"), indent=2, ensure_ascii=False)
json.dump(articles, open("articles.json", "w"), indent=2, ensure_ascii=False)

print(f"✔️ {len(articles)} novas notícias coletadas")

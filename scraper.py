import requests, json, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = "https://www.bbc.com/portuguese"
HEADERS = {"User-Agent": "Mozilla/5.0"}

resp = requests.get(URL, headers=HEADERS, timeout=15)
soup = BeautifulSoup(resp.text, "html.parser")

articles = []

links = set()

for a in soup.select("a[href]"):
    href = a["href"]

    if "/portuguese/articles/" not in href:
        continue

    url = urljoin("https://www.bbc.com", href)

    if url in links:
        continue

    links.add(url)

    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        psoup = BeautifulSoup(r.text, "html.parser")
    except:
        continue

    title = psoup.find("h1")
    ps = psoup.find_all("p")
    img = psoup.find("meta", property="og:image")

    if not title or len(ps) < 2:
        continue

    image = img["content"] if img else ""

    articles.append({
        "title": title.text.strip(),
        "summary": " ".join(p.text.strip() for p in ps[:3]),
        "url": url,
        "image": image
    })

    if len(articles) >= 12:
        break

json.dump(articles, open("articles.json","w"), indent=2, ensure_ascii=False)

print("✔️ matérias coletadas:", len(articles))

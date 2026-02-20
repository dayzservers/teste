import json
import os

articles = json.load(open("articles.json")) if os.path.exists("articles.json") else []

featured = articles[0] if articles else None
rest = articles[1:] if len(articles) > 1 else []

cards = ""
for a in rest:
    img = f'<img src="{a.get("image","")}" loading="lazy">' if a.get("image") else ""
    cards += f"""
    <article class="card">
      {img}
      <div class="card-content">
        <h2>{a['title']}</h2>
        <p>{a['summary']}</p>
        <a href="{a['url']}" target="_blank">Ler matéria →</a>
      </div>
    </article>
    """

featured_html = ""
if featured:
    img = f'<img src="{featured.get("image","")}">' if featured.get("image") else ""
    featured_html = f"""
    <section class="featured">
        {img}
        <div class="featured-text">
            <h2>{featured['title']}</h2>
            <p>{featured['summary']}</p>
            <a href="{featured['url']}" target="_blank">Ler matéria</a>
        </div>
    </section>
    """

html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Notícias em Destaque</title>

<meta name="description" content="Resumo automático das principais notícias">
<meta property="og:title" content="Notícias em Destaque">
<meta property="og:type" content="website">

<link rel="stylesheet" href="style.css">
<script defer src="app.js"></script>
</head>

<body>

<header class="topbar">
    <h1>📰 Notícias</h1>

    <div class="actions">
        <input id="search" placeholder="Buscar notícia...">
        <button id="themeToggle">🌙</button>
    </div>
</header>

{featured_html}

<main class="container">
    {cards}
</main>

<button id="topBtn">↑</button>

<footer>
    Fonte: BBC Brasil • Resumo automático
</footer>

</body>
</html>
"""

open("index.html", "w").write(html)

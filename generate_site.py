import json, os

articles = json.load(open("articles.json")) if os.path.exists("articles.json") else []

cards = ""
for a in articles:
    img = f'<img src="{a["image"]}" loading="lazy">' if a.get("image") else ""
    cards += f"""
    <article class="card">
        {img}
        <div class="card-body">
            <h2>{a['title']}</h2>
            <p>{a['summary']}</p>
            <a href="{a['url']}" target="_blank">Ler na BBC</a>
        </div>
    </article>
    """

html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Portal de Notícias</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <h1>📰 Portal de Notícias</h1>
    <p>Resumo automático das principais notícias</p>
</header>

<main class="grid">
    {cards}
</main>

<footer>
    Fonte: BBC Brasil
</footer>

</body>
</html>
"""

open("index.html","w").write(html)

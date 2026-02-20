import json
import os

articles = json.load(open("articles.json")) if os.path.exists("articles.json") else []

cards = ""
for a in articles:
    cards += f"""
    <article class="card">
      <h2>{a['title']}</h2>
      <p>{a['summary']}</p>
      <a href="{a['url']}" target="_blank">Ler na BBC →</a>
    </article>
    """

html = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Notícias em Destaque</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Resumo automático das principais notícias da BBC Brasil">
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header class="hero">
      <div class="hero-content">
          <h1>📰 Notícias em Destaque</h1>
          <p>Resumo automático das principais notícias da BBC Brasil</p>
      </div>
  </header>

  <main class="container">
      {cards}
  </main>

  <footer>
      <p>Fonte: BBC Brasil • Conteúdo resumido automaticamente</p>
  </footer>

</body>
</html>
"""

open("index.html", "w").write(html)

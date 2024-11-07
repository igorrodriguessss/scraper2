import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# Buscar todas as notícias
noticias = site.find_all('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    # Extrair o título
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    if titulo:
        print(titulo.text)  # Extrai o texto do título

    # Extrair o subtítulo
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    if subtitulo:
        print(subtitulo.text)  # Extrai o texto do subtítulo

import requests
from bs4 import BeautifulSoup
resposta = requests.get('https://g1.globo.com/')

conteudo = (resposta.content)

site = BeautifulSoup(conteudo, "html.parser")

noticias = site.findAll('a', attrs={'class':'feed-post-link gui-color-primary gui-color-hover'})

for noticia in noticias:
    print(noticia.text)
    print()
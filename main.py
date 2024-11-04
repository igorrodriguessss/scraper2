import requests
from bs4 import BeautifulSoup

GREEN = "\033[92m" 
RESET = "\033[0m" 

resposta = requests.get('https://www.nyc.gov/site/nypd/index.page')

# Verificar se a requisição foi bem-sucedida
if resposta.status_code == 200:
    site = BeautifulSoup(resposta.content, 'html.parser')
    conteudo = site.find('div', attrs={'class': 'content-info-inner'})  # se a teg que está o conteúdo desejado não for uma div, troque ela pela tag desejada, o mesmo com a classe.Será necessário inspecionar o site desejado.
    print(f"{GREEN}Conteúdo da div:{RESET}")
    print(conteudo.prettify() if conteudo else "Div não encontrada.")
else:
    print(f"Erro ao acessar o site: {resposta.status_code}")

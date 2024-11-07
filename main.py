from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Inicializar o Selenium WebDriver (ajuste conforme necessário)
driver = webdriver.Chrome()

# Acessar a página desejada
driver.get('https://www.mercadolivre.com.br/')
time.sleep(5)  # Aguarda o carregamento da página

# Obter o HTML da página
html = driver.page_source
site = BeautifulSoup(html, 'html.parser')

# Buscar todos os elementos de preço
precos = site.find_all('s', class_='andes-money-amount andes-money-amount--previous andes-money-amount--cents-comma')

# Iterar sobre cada elemento de preço encontrado e exibir o texto
if precos:
    for preco in precos:
        # Verificar a existência de cada parte antes de tentar acessar o texto
        moeda = preco.find('span', class_='andes-money-amount__currency-symbol')
        parte_inteira = preco.find('span', class_='andes-money-amount__fraction')
        centavos = preco.find('span', class_='andes-money-amount__cents')

        # Extrair os textos somente se os elementos existirem
        moeda_text = moeda.text.strip() if moeda else ""
        parte_inteira_text = parte_inteira.text.strip() if parte_inteira else ""
        centavos_text = centavos.text.strip() if centavos else ""

        # Construir e imprimir o preço completo
        preco_completo = f"{moeda_text} {parte_inteira_text},{centavos_text}"
        print(preco_completo)
else:
    print("Nenhum preço encontrado.")

# Fechar o driver
driver.quit()

import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox

# Função para limpar o texto do preço e remover qualquer caractere indesejado como 'Â'
def clean_price(price):
    # Remover o caractere 'Â' e espaços extras
    return price.replace('Â', '').strip()

# Função para realizar o scraping e salvar os dados em CSV
def scrape_quotes():
    url = entry_url.get()
    filename = entry_filename.get()
    tag = entry_tag.get()
    class_name = entry_class.get()  # Obtendo a classe diretamente

    if not url or not filename or not tag or not class_name:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return

    try:
        # Fazer o pedido da página e analisar com BeautifulSoup
        page_to_scrape = requests.get(url)

        # Verificar se o pedido foi bem sucedido (status code 200)
        if page_to_scrape.status_code != 200:
            messagebox.showerror("Erro", f"Falha ao acessar a página. Status code: {page_to_scrape.status_code}")
            return

        # Analisando a página com BeautifulSoup
        soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

        # Encontrar os elementos com a tag e a classe especificadas
        elements = soup.find_all(tag, class_=class_name)

        # Verifique se encontramos algum elemento
        if not elements:
            messagebox.showerror("Erro", f"Nenhum elemento encontrado com tag '{tag}' e classe '{class_name}'.")
            return

        # Abrir um novo arquivo CSV para salvar os dados com codificação UTF-8-sig
        with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            # Criar uma linha de cabeçalho com o nome da tag e classe
            writer.writerow([f"Conteúdo da tag '{tag}' com classe '{class_name}'"])

            # Escrever o conteúdo extraído no CSV
            for element in elements:
                # Extrair o texto da tag (limpando o preço se for um valor)
                element_text = clean_price(element.text) if element else "Texto não encontrado"
                writer.writerow([element_text])

        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Scraping concluído! Dados salvos em '{filename}'.")

    except Exception as e:
        # Caso ocorra um erro
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# CRIAR A INTERFACE GRÁFICA
root = tk.Tk()
root.title("Web Scraping Personalizado")

# Definir tamanho da janela
root.geometry("500x300")

# Criar rótulos e campos de entrada
label_url = tk.Label(root, text="Digite a URL para scraping:")
label_url.pack(pady=5)

entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

label_filename = tk.Label(root, text="Digite o nome do arquivo CSV:")
label_filename.pack(pady=5)

entry_filename = tk.Entry(root, width=50)
entry_filename.pack(pady=5)

label_tag = tk.Label(root, text="Digite a tag HTML (ex: 'div', 'span'):")
label_tag.pack(pady=5)

entry_tag = tk.Entry(root, width=50)
entry_tag.pack(pady=5)

label_class = tk.Label(root, text="Digite o nome da classe (ex: 'product_price'):")
label_class.pack(pady=5)

entry_class = tk.Entry(root, width=50)
entry_class.pack(pady=5)

# Criar o botão para iniciar o scraping
button_scrape = tk.Button(root, text="Iniciar Scraping", command=scrape_quotes)
button_scrape.pack(pady=20)

# Iniciar a interface
root.mainloop()

from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Inicializar o driver do Chrome
driver = webdriver.Chrome()
driver.get("https://www.terabyteshop.com.br/pc-gamer")

# Encontrar os elementos dos títulos e preços dos produtos
titulos = driver.find_elements(By.XPATH, "//a[@class='prod-name']")
precos = driver.find_elements(By.XPATH, "//div[@class='prod-new-price']")

# Criar um novo workbook e adicionar uma nova sheet
workbook = openpyxl.Workbook()
sheet_produtos = workbook.create_sheet('produtos')
workbook.remove(workbook['Sheet'])  # Remove a sheet padrão criada automaticamente

# Adicionar cabeçalhos na planilha
sheet_produtos['A1'].value = 'produto'
sheet_produtos['B1'].value = 'preço'

# Adicionar os produtos e seus preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])

# Salvar o workbook em um arquivo
workbook.save('produtos.xlsx')

# Fechar o driver do Chrome
driver.quit()

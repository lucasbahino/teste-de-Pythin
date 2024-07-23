from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Inicializar o WebDriver
driver = webdriver.Chrome()
driver.get("https://forms.gle/caxPUM31XrN4uZxN7")
time.sleep(2)

# Carregar os dados do Excel
tabela_produtos = pd.read_excel("produtos.xlsx")

# Loop para cadastrar todos os itens do Excel
for linha in tabela_produtos.index:
    # Recarregar o formulário para cada iteração
    driver.get("https://forms.gle/caxPUM31XrN4uZxN7")
    time.sleep(2)

    # Encontrar os campos do formulário
    produto_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    preco_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    enviar_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    # Obter os dados da linha
    produto = tabela_produtos.loc[linha, "produto"]
    preco = tabela_produtos.loc[linha, "preço"]

    # Preencher o formulário
    produto_field.send_keys(produto)
    preco_field.send_keys(preco)

    # Clicar no botão de enviar
    enviar_button.click()

    # Esperar alguns segundos para evitar problemas com o carregamento do formulário
    time.sleep(2)

# Esperar alguns segundos para ver o resultado
time.sleep(5)

# Fechar o navegador
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://pt-br.facebook.com/login/device-based/regular/login/")

email_field = driver.find_element(By.ID, 'email')
password_field = driver.find_element(By.ID, 'pass')
login_button = driver.find_element(By.NAME, 'login')

email_field.send_keys('seu_email_aqui')
password_field.send_keys('sua_senha_aqui')

login_button.click()

time.sleep(5)

driver.quit()

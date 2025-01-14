from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://campusvirtualunillanos.co")

usuarios_accediendo = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/section[2]/div/div/div[2]/div/div[1]/div/h3')

cursos = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/section[2]/div/div/div[2]/div/div[2]/div/h3')

print(usuarios_accediendo.text)
print(cursos.text)

browser.quit()

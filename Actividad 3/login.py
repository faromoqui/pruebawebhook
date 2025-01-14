from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get("https://demo.guru99.com/test/login.html")

correo = browser.find_element(By.ID, "email")
correo.clear()
correo.send_keys('correo@yahoo.es')
password = browser.find_element(By.ID, "passwd")
password.clear()
password.send_keys('yahoo123')
submitButton = browser.find_element(By.ID, 'SubmitLogin')
submitButton.send_keys(Keys.ENTER)

try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()

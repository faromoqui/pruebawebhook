from selenium import webdriver
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("https://campusvirtualunillanos.co/")
time.sleep(2) #Mostrar despues
browser.execute_script("window.open('');") #Carga en background el primero
time.sleep(2)
browser.switch_to.window(browser.window_handles[1]) #Para abrir una ventana nueva 1, porque ya se abrio la cero
time.sleep(2)
browser.get("https://tucarro.com/")
browser.execute_script("window.open('');") #Carga en background el primero
time.sleep(2)
browser.switch_to.window(browser.window_handles[2]) 
browser.get("https://www.mercadolibre.com.co/")
browser.switch_to.window(browser.window_handles[0]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[1]) 
time.sleep(2)
browser.switch_to.window(browser.window_handles[2]) 

#browser.quit()


try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()
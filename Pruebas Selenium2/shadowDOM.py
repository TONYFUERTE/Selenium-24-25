from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost:3000')

driver.find_element(By.LINK_TEXT, "ShadowDOM").click()

#Seleccionamos el contenedor
contenedorShadowHost = driver.find_element(By.ID, "nodoShadowHost")
shadow_root = driver.execute_script("return arguments[0].shadowRoot",contenedorShadowHost)
botonShadow = shadow_root.find_element(By.ID, "boton2")
botonShadow.click()

print(shadow_root.find_element(By.ID, "resultado").text)

time.sleep(100)
driver.quit()
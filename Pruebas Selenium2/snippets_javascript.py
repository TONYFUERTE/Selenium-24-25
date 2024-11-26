from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost:3000')

driver.find_element(By.LINK_TEXT, "XPaths").click()
time.sleep(1)
botones = driver.find_elements(By.TAG_NAME, "button")
# print(len(botones))
print(botones[10].location["x"])
#Movemos el scroll hacia abajo hasta la posición del botón 10
driver.execute_script("window.scrollBy(0,arguments[0])",botones[10].location["y"])

#Podemos ejecutar un alert por ejemplo
driver.execute_script("alert('Soy un alert implementado desde Selenium')")
time.sleep(3)
driver.switch_to.alert.accept()

time.sleep(100)
driver.quit()

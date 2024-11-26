from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://localhost:3000')

driver.find_element(By.LINK_TEXT,"Checkboxes").click()
print(len(driver.find_elements(By.TAG_NAME, "input")))


lista = driver.find_elements(By.TAG_NAME, "input")
# for i in lista:
#     i.click()

print(lista[2].is_selected())
print(lista[2].is_enabled())

driver.find_element(By.ID, "enviarCheckboxbutton").click()
print(driver.find_element(By.ID,"resultado").text)
time.sleep(100)
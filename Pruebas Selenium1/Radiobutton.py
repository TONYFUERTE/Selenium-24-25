from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://localhost:3001')
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, "Radiobuttons").click()

driver.find_element(By.XPATH, "//input[@value='agua']").click()
driver.find_element(By.XPATH, "//input[@value='dorada']").click()
bebidas = driver.find_elements(By.XPATH, "//input[@name='bebida']")
for i in bebidas:
    print(i.get_attribute("value"))

driver.find_element(By.ID, "enviarRadiobutton").click()

print(driver.find_element(By.ID, "resultado").text)


time.sleep(100)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from random import randint

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10,0.2)

driver.get('http://localhost:3000/')

driver.find_element(By.XPATH, "//nav/a[text()='Checkboxes']").click()
driver.implicitly_wait(10)

check_boxes = driver.find_elements(By.XPATH, "//input[contains(@name,'listaCompra')]")
print(check_boxes)

number_of_boxes_to_select = randint(1, (len(check_boxes) - 1))
print(number_of_boxes_to_select)

while number_of_boxes_to_select > 0:
    index = number_of_boxes_to_select
    check_boxes[index].click()
    number_of_boxes_to_select -= 1

driver.find_element(By.ID, "enviarCheckboxbutton").click()

result = driver.find_element(By.ID, "resultado").text
print(result)

time.sleep(100)

driver.quit()
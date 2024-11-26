from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost:3000')

driver.find_element(By.PARTIAL_LINK_TEXT, "Alert").click()

driver.find_element(By.ID, "buttonAlertSimple").click()
driver.switch_to.alert.accept()
time.sleep(3)

driver.find_element(By.ID, "buttonAlertConfirm").click()
driver.switch_to.alert.dismiss()
time.sleep(3)

driver.find_element(By.ID, "buttonAlertPrompt").click()
driver.switch_to.alert.send_keys("Hola desde el alert")
driver.switch_to.alert.accept()

time.sleep(10)
driver.quit()
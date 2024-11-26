from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost:3000')

driver.find_element(By.PARTIAL_LINK_TEXT, "Calendars").click()
fecha = driver.find_element(By.NAME, "fecha")
fecha.send_keys("20112024")
fecha.send_keys(Keys.TAB)
fecha.send_keys("22:31")

print(fecha.get_attribute("value"))

time.sleep(100)
driver.quit()
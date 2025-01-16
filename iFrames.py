from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost:3000')

driver.find_element(By.LINK_TEXT, "iFrames").click()
#IFRAME 1
driver.switch_to.frame("inception_1")
driver.find_element(By.ID, "iframebutton").click()
time.sleep(5)

#IFRAME 2
driver.switch_to.frame("inception_2")
driver.find_element(By.ID, "iframebutton").click()

driver.switch_to.default_content()
time.sleep(100)

driver.quit()

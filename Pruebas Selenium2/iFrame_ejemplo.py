from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.w3schools.com/html/html_iframe.asp')
#Aceptar cookies
driver.find_element(By.ID, "accept-choices").click()
iframe = driver.find_element(By.XPATH, "//iframe[@title='W3Schools HTML Tutorial']")
driver.switch_to.frame(iframe)
driver.find_element(By.ID, "accept-choices").click()
# time.sleep(100)
# print(len(driver.find_elements(By.XPATH, "//a[@title='JavaScript Tutorial']")))
enlaces = driver.find_elements(By.XPATH, "//a[@title='JavaScript Tutorial']")
enlaces[2].click()


time.sleep(100)
driver.quit()
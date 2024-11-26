from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.get("http://localhost:3000")


driver.find_element(By.LINK_TEXT, "Waits").click();

driver.find_element(By.ID, "implicitWaitButton").click();

driver.find_element(By.ID, "explicitWaitButton").click()

wait = WebDriverWait(driver,10,0.2)
button = (By.ID, "explicitWaitButton");
button_ex_wait = wait.until(EC.element_to_be_clickable(button)).click()

time.sleep(100)

driver.quit()


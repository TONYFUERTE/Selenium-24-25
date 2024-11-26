from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1424, 768) 
driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
driver.find_element(By.ID, "searchInput").send_keys("Canarias")
driver.find_element(By.ID, "searchInput").send_keys(Keys.RETURN)
# driver.find_element(By.XPATH, "//button[@class='cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button']").click()

print(driver.title)
assert("Canarias - Wikipedia, la enciclopedia " == driver.title), "El texto no coincide con el título"
time.sleep(20)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://localhost:3001")
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, "Comboboxes").click()
select = Select(driver.find_element(By.ID, "combobox1"))
select.select_by_index(0)
# for i in select.options:
#     print(i.text)
#     print(i.get_attribute("value"))

select2 = Select(driver.find_element(By.ID, "combobox2"))
select2.select_by_visible_text("Manzana")
select2.select_by_visible_text("Granada")

driver.find_element(By.ID, "enviaComboboxes").click()

print(driver.find_element(By.ID,"resultado").text)



time.sleep(100)

driver.quit()
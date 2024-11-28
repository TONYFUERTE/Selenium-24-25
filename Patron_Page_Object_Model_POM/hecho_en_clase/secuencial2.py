import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class test_CIFP_Majada(unittest.TestCase):
        
    
    def test_busqueda_google(self):
        
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        driver.implicitly_wait(10)
        
        #GOOGLE
        #Rechazar cookies
        driver.find_element(By.XPATH, "//div[text()='Rechazar todo']/ancestor::button").click()
        driver.find_element(By.NAME, 'q').send_keys('CIFP MAJADA MARCIAL')
        driver.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
        print(driver.title)
        assert 'CIFP MAJADA MARCIAL - Buscar con Google' in driver.title
        #Click a la primera búsqueda
        driver.find_element(By.XPATH, "//h3[1]/ancestor::a[1]").click()
        
        #MAJADA
        
        driver.find_element(By.XPATH, "//a[text()='Estudios'][1]").click()
        driver.execute_script("window.scrollBy(0,arguments[0])",500)
        # time.sleep(3)
        driver.find_element(By.LINK_TEXT, "Informática y comunicaciones").click()

        time.sleep(1000)

# time.sleep(1000)


if __name__ == "__main__":
    unittest.main()
    
    
    
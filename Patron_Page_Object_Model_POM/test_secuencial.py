import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class prueba_pom(unittest.TestCase):
    
    def test_wikipedia_articulo_bueno(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        
        driver.get("https://www.google.com")
        #Rechazar cookies
        # time.sleep(1000)
        driver.find_element(By.XPATH, "//div[text()='Rechazar todo']/ancestor::button").click()
        #Barra de búsqueda
        search_bar = driver.find_element(By.NAME, "q")
        search_bar.send_keys("wikipedia")
        search_bar.send_keys(Keys.RETURN)
        # time.sleep(1)
        assert "wikipedia - Buscar con Google" in driver.title 
        #Se pulsa el primer enlace que se obtiene en la búsqueda
        driver.find_element(By.XPATH, "//div[@id='search']/descendant::div[@class='g'][1]/descendant::a[1]").click()
        # time.sleep(1)

        assert "Wikipedia, la enciclopedia libre" in driver.title
        
        print(driver.find_element(By.XPATH, "//div[@id='Artículo_bueno']/following-sibling::h2/descendant::a").get_attribute("title"))
        
        # time.sleep(3)
        #Obtenemos el título del artículo bueno a través del enlace
        titulo =  driver.find_element(By.XPATH, "//div[@id='Artículo_bueno']/following-sibling::h2/descendant::a").get_attribute("title")
        assert "Bohemundo VI de Antioquía" in titulo
        driver.quit()
        # time.sleep(100)  

        
if __name__=="__main__":
    unittest.main()
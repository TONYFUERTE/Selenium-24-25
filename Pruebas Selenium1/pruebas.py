from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

class PruebasUnittest(unittest.TestCase):
    
    def setUp(self):
        print('Este método se ejecuta antes de cada test.')
        self.driver = webdriver.Chrome()
        pass
    
    def test_a(self):
        print('Ejecutando el test a')
        self.driver.get('https://www.google.com')
        self.assertEqual(self.driver.title, "Gogleeerrrr") 
        time.sleep(10)
        pass
    
    def test_b(self):
        print('Ejecutando el test b')
        self.driver.get('https://www.google.com')
        #Rechazar cookies
        contenedor = self.driver.find_element(By.CLASS_NAME, "jw8mI")
        self.driver.find_element(By.ID, 'W0wltc').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        # print(contenedor)
        boton = self.driver.find_element(By.XPATH,"//div[text()='Rechazar todo']")
        # self.driver.execute_script("window.scrollBy(0,arguments[0])", boton.location["y"])
        # driver.execute_script("window.scrollBy(0,arguments[0])",botones[10].location["y"])
        self.driver.find_element(By.XPATH,"//div[text()='Rechazar todo']").click()

        self.driver.find_element(By.NAME,"q").send_keys('wikipedia')
        self.driver.find_element(By.NAME,"q").send_keys(Keys.RETURN)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"es.wikipe").click()
        self.assertEqual(self.driver.title, "Wikipedia, la enciclopedia libertario"), "El título no es correcto"
        time.sleep(100)
        pass
    
    def tearDown(self):
        print('Este método se ejecuta después de cada test')
        pass

if __name__ == "__main__":
    unittest.main()
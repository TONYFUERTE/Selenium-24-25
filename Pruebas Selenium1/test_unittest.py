import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

class PruebaSelenium(unittest.TestCase):
    
    def setUp(self):
        print('Me ejecuto antes de cada test.')
        self.driver = webdriver.Chrome()
        pass
    
    def test_a(self):
        print('Me ejecuto en el test A')
        self.driver.get("https://www.google.com")
        time.sleep(2)
        self.assertEqual("Google", self.driver.title)
        pass
    
    def test_b(self):
        print('Me ejecuto en el test B')
        # self.driver.implicitly_wait(10)
        #GOOGLE
        self.driver.get("https://www.google.com")
        #Aceptamos cookies
        # time.sleep(100)
        self.driver.find_element(By.XPATH, "//div[text()='Rechazar todo']/ancestor::button").click()
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys("wikipedia")
        search_bar.send_keys(Keys.RETURN)
        #WIKIPEDIA
        self.driver.find_element(By.XPATH, "//a[@jsname='UWckNb'][1]").click()
        self.assertEqual(self.driver.title, "Wikipedia, la enciclopedia libre")
        # time.sleep(100)
        pass
    
    def tearDown(self):
        print('Me ejecuto después de cada test. ')
        self.driver.quit()
        pass
    
if __name__ == "__main__":
    unittest.main()
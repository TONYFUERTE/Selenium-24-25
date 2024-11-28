import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pages
import time

class prueba_pom(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.google.com")
    
    def test_wikipedia_articulo_bueno(self):
        
        texto_a_buscar = 'Wikipedia'
        
        #GOOGLE PAGE
        google_page = pages.GooglePage(self.driver)
        google_page.refuse_cookies()
        google_page.search_for_string(texto_a_buscar)
        
        #SEARCH RESULTS GOOGLE PAGE
        search_result_page = pages.SearchResultsPage(self.driver)
        assert search_result_page.we_are_on_result_page(texto_a_buscar), "No estamos en la página de resultados"
        # titulo_resultados = pages.BasePage(self.driver)
        # print(titulo_resultados.get_title())
        # assert  titulo_resultados.get_title() == "Wikipedia - Buscar con Google", "No estamos en la página de resultados"
        search_result_page.click_on_first_result()
        
        #WIKIPEDIA PAGE
        wikipedia_page = pages.Wikipedia(self.driver)
        title = wikipedia_page.get_title_Articulo_Bueno()
        assert "After Midnight" in title
    
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    unittest.main()
        
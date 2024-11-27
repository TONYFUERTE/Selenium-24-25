from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        
    def get_title(self):
        return self.driver.title

class GooglePage(BasePage):
    refuse_cookies_button = (By.XPATH, "//div[text()='Rechazar todo']/ancestor::button")
    
    def refuse_cookies(self):
        self.driver.find_element(*self.refuse_cookies_button).click()
        
    def search_for_string(self, string_to_search):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys(string_to_search)
        search_bar.send_keys(Keys.RETURN)
        
class SearchResultsPage(BasePage):
    
    first_result = (By.XPATH, "//div[@id='search']/descendant::div[@class='g'][1]/descendant::a[1]")
    
    def click_on_first_result(self):
        self.driver.find_element(*self.first_result).click()
        
    def we_are_on_result_page(self,texto_buscado):
        return str(texto_buscado + " - Buscar con Google") in self.driver.title 
        
class Wikipedia(BasePage):
    articulo_bueno = (By.XPATH, "//div[@id='Artículo_bueno']/following-sibling::h2/descendant::a")
    
    def get_title_Articulo_Bueno(self):
        return self.driver.find_element(*self.articulo_bueno).get_attribute("title")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def obtener_titulo(self):
        self.driver.title()
        
class PaginaGoogle(BasePage):
    rechazar_c = (By.XPATH, "//div[text()='Rechazar todo']/ancestor::button")
    primer_elemento = (By.XPATH, "//h3[1]/ancestor::a[1]")
    caja_texto = (By.NAME, 'q')
    
    def rechazar_Cookies(self):
        self.driver.find_element(*self.rechazar_c).click()
    
    def busqueda (self,texto_busqueda):
        search_bar = self.driver.find_element(*self.caja_texto)
        search_bar.send_keys(texto_busqueda) 
        search_bar.send_keys(Keys.RETURN) 
        
    def pulsar_primera_busqueda(self):
        self.driver.find_element(*self.primer_elemento).click()
        
class CifpMajada(BasePage):
    
    def entrar_apartado_menu (self,apartado):
        self.driver.find_element(By.LINK_TEXT, f"{apartado}").click()
        
    def entrar_subapartado (self,subapartado):
        self.driver.find_element(By.LINK_TEXT, f"{subapartado}").click()
    
    def hacer_scroll (self,coordenada_y):
        self.driver.execute_script("window.scrollBy(0,arguments[0])",coordenada_y)
    
    def comprobar_que_hay_ciclos(self,subapartado):
        lista_ciclos = self.driver.find_elements(By.XPATH, "//div[@class='et_pb_text_inner']/descendant::p")
        print("\n" + subapartado.upper() + ": ")
        for i in lista_ciclos:
            print(i.text)
        return lista_ciclos
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pages2
import time

class prueba_pom(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.google.com")
        
    def test_busqueda_estudios_majada (self):
        
        #GOOGLE
        entrada = 'cifp majada marcial'
        google_procces = pages2.PaginaGoogle(self.driver)
        google_procces.rechazar_Cookies()
        google_procces.busqueda(entrada)
        google_procces.pulsar_primera_busqueda()

        #MAJADA
        apartado_menu = 'Estudios'
        subapartado = 'Informática y comunicaciones'
        coordenada_y = 500
        majada = pages2.CifpMajada(self.driver)
        majada.entrar_apartado_menu(apartado_menu)
        majada.entrar_subapartado(subapartado)
        majada.hacer_scroll(coordenada_y)
        
        #Verificar que hay especialidades en el subapartado de Estudios
        listado_ciclos = majada.comprobar_que_hay_ciclos(subapartado)
        assert listado_ciclos, "No hay ningún ciclo en este apartado"
        
        time.sleep(3)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



    
    
    
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re 

class RegistroPrueba(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_registro_exito(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("usuario prueba")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("usuarioExito")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("123456789")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("123456789")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        URL = self.driver.current_url
        #Cambia hacia login si registro exitoso
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" );

    def test_registro_vacios(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );

    def test_registro_nombreMax(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        for x in range(0,50):
            driver.find_element_by_id("fUsuario_nombre").send_keys('a')  
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("nombreMax")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("123456789")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("123456789")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario1@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Cambia hacia login si registro exitoso
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" ); 

    def test_registro_nombreMayor(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        for x in range(0,51):
            driver.find_element_by_id("fUsuario_nombre").send_keys('a')  
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("nombreMayor")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("123456789")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("123456789")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario2@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );

    def test_registro_nombreVacio(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("nombreVacio")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("123456789")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("123456789")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario3@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );

    def test_registro_usuarioVacio(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("usuarioVacio")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("123456789")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("123456789")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario4@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );

    def test_registro_usuarioMax(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("usuarioMax")
        driver.find_element_by_id("fUsuario_usuario").clear()
        for x in range(0,15):
            driver.find_element_by_id("fUsuario_usuario").send_keys('a')
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("123456789")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("123456789")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario5@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Cambia hacia login si registro exitoso
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" ); 

    def test_registro_usuarioMayor(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("usuarioMayor")
        driver.find_element_by_id("fUsuario_usuario").clear()   
        for x in range(0,16):
            driver.find_element_by_id("fUsuario_usuario").send_keys('a')               
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("123456789")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("123456789")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario6@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );

    def test_registro_usuarioExistente(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("usuarioMayor")
        driver.find_element_by_id("fUsuario_usuario").clear()   
        driver.find_element_by_id("fUsuario_usuario").send_keys("usuarioExito")               
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("123456789")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("123456789")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario7@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );

    def test_registro_claveMayor(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("claveMayor")
        driver.find_element_by_id("fUsuario_usuario").clear()  
        driver.find_element_by_id("fUsuario_usuario").send_keys("claveMayor")               
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave2").clear()
        for x in range(0,17):
            driver.find_element_by_id("fUsuario_clave").send_keys('a')        
            driver.find_element_by_id("fUsuario_clave2").send_keys('a')
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario8@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );

    def test_registro_claveMax(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("claveMax")
        driver.find_element_by_id("fUsuario_usuario").clear()  
        driver.find_element_by_id("fUsuario_usuario").send_keys("claveMax")               
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave2").clear()
        for x in range(0,16):
            driver.find_element_by_id("fUsuario_clave").send_keys('a')        
            driver.find_element_by_id("fUsuario_clave2").send_keys('a')
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario9@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Cambia hacia login si registro exitoso
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" ); 

    def test_registro_claveMenor(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("claveMenor")
        driver.find_element_by_id("fUsuario_usuario").clear()  
        driver.find_element_by_id("fUsuario_usuario").send_keys("claveMenor")               
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave2").clear()
        for x in range(0,7):
            driver.find_element_by_id("fUsuario_clave").send_keys('a')        
            driver.find_element_by_id("fUsuario_clave2").send_keys('a')
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario10@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );

    def test_registro_claveMin(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("claveMin")
        driver.find_element_by_id("fUsuario_usuario").clear()  
        driver.find_element_by_id("fUsuario_usuario").send_keys("claveMin")               
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave2").clear()
        for x in range(0,8):
            driver.find_element_by_id("fUsuario_clave").send_keys('a')        
            driver.find_element_by_id("fUsuario_clave2").send_keys('a')
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("usuario11@mail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)      
        URL = self.driver.current_url
        #Cambia hacia login si registro exitoso
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" );

    def test_registro_correoVacio(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("correoVacio")
        driver.find_element_by_id("fUsuario_usuario").clear()  
        driver.find_element_by_id("fUsuario_usuario").send_keys("correoVacio")               
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("correoVacio")        
        driver.find_element_by_id("fUsuario_clave2").send_keys("correoVacio")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)    
        URL = self.driver.current_url
        #Se queda en la pagina de registro si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VRegistro" );


    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
     unittest.main(verbosity=2)

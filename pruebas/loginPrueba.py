# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re 

class loginPrueba(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/#/VLogin"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_exito(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()        
        driver.find_element_by_id("fLogin_usuario").send_keys("usuarioExito")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("123456789")
        driver.find_element_by_xpath("//button[@type='submit']").click()        
        URL = self.driver.current_url
        #Cambia hacia principal si login fue exitoso
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VPrincipal" );

    def test_login_vacio(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()        
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_xpath("//button[@type='submit']").click()        
        URL = self.driver.current_url
        #Se queda en la pagina de login si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" );    

    def test_login_usuarioVacio(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()        
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("123456789")
        driver.find_element_by_xpath("//button[@type='submit']").click()        
        URL = self.driver.current_url
        #Se queda en la pagina de login si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" );    

    def test_login_claveVacio(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear() 
        driver.find_element_by_id("fLogin_usuario").send_keys("usuarioExito")       
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_xpath("//button[@type='submit']").click()        
        URL = self.driver.current_url
        #Se queda en la pagina de login si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" );

    def test_login_usuarioMal(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear() 
        driver.find_element_by_id("fLogin_usuario").send_keys("usuarioMal")       
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("123456789")
        driver.find_element_by_xpath("//button[@type='submit']").click()        
        URL = self.driver.current_url
        #Se queda en la pagina de login si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" );

    def test_login_claveMal(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()        
        driver.find_element_by_id("fLogin_usuario").send_keys("usuarioExito")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("123456789Mal")
        driver.find_element_by_xpath("//button[@type='submit']").click()        
        URL = self.driver.current_url
        #Se queda en la pagina de login si hay error
        self.assertEquals(URL, "http://0.0.0.0:8080/#/VLogin" );
    
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

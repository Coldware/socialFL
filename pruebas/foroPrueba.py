# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class foroPrueba(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True

    
    def test1_crearForo(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Foros").click()
        time.sleep(2)
        driver.find_element_by_id("fForo_titulo").clear()
        driver.find_element_by_id("fForo_titulo").send_keys("Foro Prueba")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2) 
        # Vemos da el msj de creado
        elem = driver.find_element_by_css_selector("li.success")
        #print('ELEMENTO TEXT')
        #print(elem.text)   
        self.assertEquals(elem.text, 'Foro creado')        
        # Vemos si se ve
        elem = driver.find_element_by_css_selector("td.ng-binding")
        #print('ELEMENTO TEXT')
        #print(elem.text)
        self.assertEquals(elem.text, "Foro Prueba") 
        

    def test2_crearForo_mismoNombre(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Foros").click()
        time.sleep(2)
        # Crear foro con el mismo nombre (Debe dar error) 
        driver.find_element_by_id("fForo_titulo").clear()
        driver.find_element_by_id("fForo_titulo").send_keys("Foro Prueba")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)          
        elem = driver.find_element_by_css_selector("li.success")
        #print('ELEMENTO TEXT')
        #print(elem.text)   
        # Vemos msj de error
        self.assertEquals(elem.text, 'No se pudo crear el foro') 

    def test3_verForo_otroUsuario(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("shamuel")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Foros").click()
        time.sleep(2)        
        # Vemos si se ve
        elem = driver.find_element_by_css_selector("td.ng-binding")
        #print('ELEMENTO TEXT')
        #print(elem.text)
        self.assertEquals(elem.text, "Foro Prueba")

    def test4_elimForo_otroUsuario(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("shamuel")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Foros").click()
        time.sleep(2)        
        # Vemos si se ve
        elem = driver.find_element_by_css_selector("td.ng-binding")
        #print('ELEMENTO TEXT')
        #print(elem.text)
        self.assertEquals(elem.text, "Foro Prueba")
        # Abrimos foro y lo tratamos de eliminar (Debe dar error porque no es el autor)
        driver.find_element_by_link_text("Seleccionar").click()
        time.sleep(2) 
        driver.find_element_by_link_text("Eliminar foro").click()
        time.sleep(2) 
        elem = driver.find_element_by_css_selector("li.success")
        #print('ELEMENTO TEXT')
        #print(elem.text)   
        # Vemos msj de error
        self.assertEquals(elem.text, 'No se pudo eliminar el foro') 

    def test5_elimForo(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Foros").click()
        time.sleep(2)        
        # Vemos si se ve
        elem = driver.find_element_by_css_selector("td.ng-binding")
        #print('ELEMENTO TEXT')
        #print(elem.text)
        self.assertEquals(elem.text, "Foro Prueba")
        # Abrimos foro y lo tratamos de eliminar 
        driver.find_element_by_link_text("Seleccionar").click()
        time.sleep(2) 
        driver.find_element_by_link_text("Eliminar foro").click()
        time.sleep(2) 
        elem = driver.find_element_by_css_selector("li.success")
        #print('ELEMENTO TEXT')
        #print(elem.text)   
        # Vemos msj de exito
        self.assertEquals(elem.text, 'Foro eliminado') 


        

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

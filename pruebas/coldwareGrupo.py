# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class ColdwareGrupo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True 

    def test1_crearGrupo(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        driver.find_element_by_id("fGrupo_nombre").clear()
        driver.find_element_by_id("fGrupo_nombre").send_keys("Coldware")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        # Vemos da el msj de creado
        elem = driver.find_element_by_css_selector("li.success")
        #print('ELEMENTO TEXT')
        #print(elem.text)   
        self.assertEquals(elem.text, 'Grupo agregado')        
   

    def test_agregarMiembros(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        driver.find_element_by_link_text("Modificar grupo").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Daniela")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Douglas")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Francisco")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Jose")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Manuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)

    def test_agregarMiembros(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        driver.find_element_by_link_text("Modificar grupo").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Daniela")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Douglas")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Francisco")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Jose")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Manuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)             


    def test_elimMiembros(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        time.sleep(2)
        driver.find_element_by_link_text("Modificar grupo").click()
        time.sleep(2)       
        driver.find_element_by_link_text("Eliminar").click()
        time.sleep(2)
        driver.find_element_by_link_text("Eliminar").click()
        time.sleep(2)
        driver.find_element_by_link_text("Eliminar").click()
        time.sleep(2)
        driver.find_element_by_link_text("Eliminar").click()
        time.sleep(2)
        driver.find_element_by_link_text("Eliminar").click()
        time.sleep(2)
        driver.find_element_by_link_text("Eliminar").click()
        time.sleep(2)
        driver.find_element_by_link_text("Eliminar").click()
        time.sleep(2)

    def test_verMiembros(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        time.sleep(2)
        driver.find_element_by_link_text("Modificar grupo").click()
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Daniela")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Douglas")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Francisco")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Jose")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Manuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fMiembro_nombre")).select_by_visible_text("Vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)

    # Verifica que el chat Grupo funciona
    def test_verMiembros_Chat(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()  
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_xpath("(//a[contains(text(),'chat')])[8]").click()
        time.sleep(2)
        driver.find_element_by_id("fChat_texto").clear()
        driver.find_element_by_id("fChat_texto").send_keys("prueba mensaje")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul[2]/li[4]/a").click()
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("douglas")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()  
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_xpath("(//a[contains(text(),'chat')])[8]").click()        
        contenChat = driver.find_element_by_css_selector("li.ng-binding.ng-scope")
        #print(contenChat.text)
        if 'prueba mensaje' in contenChat.text: # Vemos si el msj aparece
            verif = 'Exito'
        else:
            verif = 'Error'
        self.assertEquals(verif,'Exito')
        driver.find_element_by_id("fChat_texto").clear()
        driver.find_element_by_id("fChat_texto").send_keys("test msj")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul[2]/li[4]/a").click()
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("shamuel")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()  
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_xpath("(//a[contains(text(),'chat')])[8]").click()
        contenChat = driver.find_elements_by_css_selector("li.ng-binding.ng-scope") 
        #print(contenChat[1].text)
        if 'test msj' in contenChat[1].text: # Vemos si el msj aparece
            verif = 'Exito'
        else:
            verif = 'Error'
        self.assertEquals(verif,'Exito')
        driver.find_element_by_id("fChat_texto").clear()
        driver.find_element_by_id("fChat_texto").send_keys("prueba exitosa")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
    
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

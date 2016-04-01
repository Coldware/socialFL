# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NuevoRegistro(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_registro_coldware(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Andres")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("andres")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("prueba@hotmail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Daniela")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("daniela")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("prueba1@hotmail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Douglas")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("douglas")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("prueba2@hotmail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Francisco")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("francisco")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("prueba3@hotmail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Jose")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("jose")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("prueba4@hotmail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Manuel")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("manuel")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("prueba5@hotmail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Shamuel")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("shamuel")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("prueba6@hotmail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_link_text("Registrarse").click()
        driver.find_element_by_id("fUsuario_nombre").clear()
        driver.find_element_by_id("fUsuario_nombre").send_keys("Vanessa")
        driver.find_element_by_id("fUsuario_usuario").clear()
        driver.find_element_by_id("fUsuario_usuario").send_keys("vanessa")
        driver.find_element_by_id("fUsuario_clave").clear()
        driver.find_element_by_id("fUsuario_clave").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_clave2").clear()
        driver.find_element_by_id("fUsuario_clave2").send_keys("prueba12")
        driver.find_element_by_id("fUsuario_correo").clear()
        driver.find_element_by_id("fUsuario_correo").send_keys("prueba7@hotmail.com")
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

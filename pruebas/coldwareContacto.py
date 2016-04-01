# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ColdwareContacto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    # Hace contactos a todo los usuarios 
    def test_contactos_coldware(self):
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
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("daniela")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2) 
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("douglas")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("francisco")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("jose")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("manuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul/li[4]/a/i").click()
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("daniela")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("douglas")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("francisco")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("jose")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("manuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul/li[4]/a/i").click()
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("douglas")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("francisco")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("jose")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("manuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul/li[4]/a/i").click()
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("francisco")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("jose")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("manuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul/li[4]/a/i").click()
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("jose")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("manuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul/li[4]/a/i").click()
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("manuel")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("shamuel")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul/li[4]/a/i").click()
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("shamuel")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        driver.find_element_by_link_text("Administrar contactos").click()
        time.sleep(2)
        Select(driver.find_element_by_id("fContacto_nombre")).select_by_visible_text("vanessa")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        

    # Verifica que los contactos fueron agregados
    def test_contactos_verificacion(self):
        driver = self.driver
        driver.get(self.base_url + "/#/VLogin")
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("vanessa")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("Contactos").click()
        time.sleep(2)
        i = 1 # Contador
        a = ['0','andres','daniela','douglas','francisco','jose','manuel','shamuel'] # Arreglo contactos      
        while i < 8: 
            if i == 1:
                elem = driver.find_element_by_css_selector("td.ng-binding")
            else:
                elem = driver.find_element_by_xpath("//tr[" + repr(i) +"]/td") 
            #print('ELEMENTO TEXT')
            #print(elem.text + ' debe ser igual ' + a[i])
            self.assertEquals(elem.text, a[i]) 
            i = i + 1


    
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

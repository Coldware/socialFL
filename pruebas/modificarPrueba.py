# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NuevoModificar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_crear_exito(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        driver.find_element_by_id("fPagina_titulo").clear()
        driver.find_element_by_id("fPagina_titulo").send_keys("Titulo Pagina Creada")
        driver.find_element_by_id("taTextElement").send_keys("Texto Pagina Creada")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul[2]/li[3]/a/i").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        time.sleep(5)
        contenPagina = driver.find_element_by_css_selector("div.ng-binding.ng-scope")        
        self.assertEquals(contenPagina.text, "Texto Pagina Creada")
        tituloPagina = driver.find_element_by_css_selector("b.ng-binding")
        self.assertEquals(tituloPagina.text, "Titulo Pagina Creada");

    def test_crear_titleVacio(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("shamuel")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        driver.find_element_by_id("fPagina_titulo").clear()
        driver.find_element_by_id("fPagina_titulo").send_keys("")
        driver.find_element_by_id("taTextElement").send_keys("Texto Pagina Creada")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        msjError = driver.find_element_by_css_selector("p.help-block")
        self.assertEquals(msjError.text, u"Error en campo Título.");

    def test_crear_tituloMenor(self): # Titulo long menor a 5, no debe crear
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("shamuel")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        driver.find_element_by_id("fPagina_titulo").clear()
        driver.find_element_by_id("fPagina_titulo").send_keys("1234")
        driver.find_element_by_id("taTextElement").send_keys("Texto Pagina Creada")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        msjError = driver.find_element_by_css_selector("p.help-block")
        self.assertEquals(msjError.text, u"Error en campo Título.");

    def test_crear_tituloMin(self): # Titulo long 5, debe crear pagina
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("shamuel")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        driver.find_element_by_id("fPagina_titulo").clear()
        driver.find_element_by_id("fPagina_titulo").send_keys("12345")
        driver.find_element_by_id("taTextElement").send_keys("Texto Pagina Creada")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul[2]/li[3]/a/i").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        time.sleep(5)
        contenPagina = driver.find_element_by_css_selector("div.ng-binding.ng-scope")
        self.assertEquals(contenPagina.text, "Texto Pagina Creada")
        tituloPagina = driver.find_element_by_css_selector("b.ng-binding")
        self.assertEquals(tituloPagina.text, "12345");

    def test_modificar_exito(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        driver.find_element_by_link_text("Modificar").click()
        driver.find_element_by_id("fPagina_titulo").clear()
        driver.find_element_by_id("fPagina_titulo").send_keys("Titulo Pagina Modificada")
        driver.find_element_by_id("taTextElement").clear()
        driver.find_element_by_id("taTextElement").send_keys("Texto Pagina Modificada")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul[2]/li[3]/a/i").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        time.sleep(5)
        contenPagina = driver.find_element_by_css_selector("div.ng-binding.ng-scope")
        self.assertEquals(contenPagina.text, "Texto Pagina Modificada")
        tituloPagina = driver.find_element_by_css_selector("b.ng-binding")
        self.assertEquals(tituloPagina.text, "Titulo Pagina Modificada")



    def test_modificar_titleVacio(self): # No debe crear
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        driver.find_element_by_link_text("Modificar").click()
        driver.find_element_by_id("fPagina_titulo").clear()
        driver.find_element_by_id("fPagina_titulo").send_keys("")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        msjError = driver.find_element_by_css_selector("p.help-block")
        self.assertEquals(msjError.text, u"Error en campo Título.");

    def test_modificar_tituloMenor(self): # Titulo long menor a 5, no debe crear
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        driver.find_element_by_link_text("Modificar").click()
        driver.find_element_by_id("fPagina_titulo").clear()
        driver.find_element_by_id("fPagina_titulo").send_keys("1234")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        msjError = driver.find_element_by_css_selector("p.help-block")
        self.assertEquals(msjError.text, u"Error en campo Título.");

    def test_modificar_tituloMin(self): # Titulo long 5, debe crear pagina
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("fLogin_usuario").clear()
        driver.find_element_by_id("fLogin_usuario").send_keys("andres")
        driver.find_element_by_id("fLogin_clave").clear()
        driver.find_element_by_id("fLogin_clave").send_keys("prueba12")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        driver.find_element_by_link_text("Modificar").click()
        driver.find_element_by_id("fPagina_titulo").clear()
        driver.find_element_by_id("fPagina_titulo").send_keys("54321")
        driver.find_element_by_id("taTextElement").clear()
        driver.find_element_by_id("taTextElement").send_keys("Texto Modificado")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='contenido-plegable']/ul[2]/li[3]/a/i").click()
        driver.find_element_by_link_text(u"Página de usuario").click()
        time.sleep(5)
        contenPagina = driver.find_element_by_css_selector("div.ng-binding.ng-scope")
        self.assertEquals(contenPagina.text, "Texto Modificado")
        tituloPagina = driver.find_element_by_css_selector("b.ng-binding")
        self.assertEquals(tituloPagina.text, "54321");


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

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUpdate():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_update(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1152, 648)
        wait = WebDriverWait(self.driver, 10)

        # Cliquer sur le bouton d'édition (adapter le sélecteur si besoin)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(6) > .btn"))).click()

        # Mettre à jour les champs du formulaire
        wait.until(EC.presence_of_element_located((By.NAME, "firstname"))).clear()
        self.driver.find_element(By.NAME, "firstname").send_keys("François")

        lastname_input = self.driver.find_element(By.NAME, "lastname")
        lastname_input.clear()
        lastname_input.send_keys("Turtle")

        email_input = self.driver.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys("mr.françois@ecoles-epsi.net")

        # Soumettre la modification
        self.driver.find_element(By.CSS_SELECTOR, ".btn-block").click()

        # Optionnel : attendre une confirmation
        # Ex: wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
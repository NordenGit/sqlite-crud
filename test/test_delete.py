import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDelete():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_delete(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1152, 648)
        wait = WebDriverWait(self.driver, 10)

        # Attendre que la table soit présente (adapter le sélecteur si besoin)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(5) > .btn"))).click()

        # Optionnel : attente ou vérification de la suppression effective
        # Ex: wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(4)")))
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCreate():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_create(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.set_window_size(1152, 648)
        wait = WebDriverWait(self.driver, 10)

        # Remplir le formulaire de création
        wait.until(EC.presence_of_element_located((By.NAME, "firstname"))).send_keys("Ludovic")
        self.driver.find_element(By.NAME, "lastname").send_keys("Edjaga Nanga")
        self.driver.find_element(By.NAME, "email").send_keys("l.edjagananga@ecoles-epsi.net")
        self.driver.find_element(By.NAME, "password").send_keys("mysecurepassword")

        # Cliquer sur le bouton submit
        self.driver.find_element(By.CSS_SELECTOR, ".btn-block").click()

        # Optionnel : attendre un élément de confirmation ou vérifier que la création a eu lieu
        # Ex: wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
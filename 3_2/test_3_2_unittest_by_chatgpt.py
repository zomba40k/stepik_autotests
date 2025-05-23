import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        time.sleep(1)
        self.browser.quit()

    def fill_form_and_submit(self, url):
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("ivan.petrov@example.com")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        return self.browser.find_element(By.TAG_NAME, "h1").text

    def test_registration1(self):
        url = "http://suninjuly.github.io/registration1.html"
        success_text = self.fill_form_and_submit(url)
        self.assertEqual("Congratulations! You have successfully registered!", success_text)

    def test_registration2(self):
        url = "http://suninjuly.github.io/registration2.html"
        success_text = self.fill_form_and_submit(url)
        self.assertEqual("Congratulations! You have successfully registered!", success_text)

if __name__ == "__main__":
    unittest.main()
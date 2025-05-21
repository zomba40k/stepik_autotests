from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_visible_text(str(int(num1.text) + int(num2.text)))

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()



finally:

    time.sleep(2)

    browser.quit()



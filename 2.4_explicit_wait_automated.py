import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element(By.CSS_SELECTOR, '#book')

    WebDriverWait(browser, 10).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'),'100'))
    button.click()
    num = browser.find_element(By.CSS_SELECTOR, '#input_value')
    num = calc(num.text)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(num)
    button = browser.find_element(By.CSS_SELECTOR, '#solve')
    button.click()

    # Забираем текст из алерта
    alert2 = browser.switch_to.alert
    alert_text = alert2.text
    time.sleep(2)
    alert2.accept()
    pyperclip.copy((alert_text.strip().split()[-1]))  # Записываю ответ из алерта в буфер обмена
finally:
    time.sleep(10)
    browser.quit()


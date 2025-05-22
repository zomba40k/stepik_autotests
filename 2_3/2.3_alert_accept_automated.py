from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyperclip #Библиотека для работы с буфером обмена
import math

def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    alert1 = browser.switch_to.alert
    alert1.accept()

    num = browser.find_element(By.CSS_SELECTOR, '#input_value')
    num = calc(num.text)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(num)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

    alert2 = browser.switch_to.alert
    alert_text = alert2.text# Текст из алерта
    time.sleep(2)
    alert2.accept()

    pyperclip.copy((alert_text.strip().split()[-1])) # Записываю ответ из алерта в буфер обмена
    time.sleep(1)
finally:

    time.sleep(5)
    browser.quit()



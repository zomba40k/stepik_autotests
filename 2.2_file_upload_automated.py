from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker #Библиотека для генерации случайных валидных значений
import os # Для работы с директориями
import pyperclip #Библиотека для работы с буфером обмена

fake = Faker() #Случайные значения

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'BIO.txt')

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    firstname.send_keys(fake.first_name())
    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lastname.send_keys(fake.last_name())
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys(fake.email())
    file = browser.find_element(By.CSS_SELECTOR, '#file')
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text# Текст из алерта
    time.sleep(2)
    alert.accept()

    pyperclip.copy((alert_text.strip().split()[-1])) # Записываю ответ из алерта в буфер обмена
    time.sleep(1)
finally:

    time.sleep(5)
    browser.quit()



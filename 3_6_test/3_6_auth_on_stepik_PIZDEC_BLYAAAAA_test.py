from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pytest
import math



try:
    with open('C:\\stepik_data\\data.txt', 'r', encoding='utf-8') as f:
        myemail = f.readline().strip()  # Читаем email
        mypassword = f.readline().strip()  # Читаем пароль
except FileNotFoundError:
    myemail = ""
    mypassword = ""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestStepik:
    num_list = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']

    def test_stepik_autotest(self, browser):

        for number in self.num_list:
            link = f'https://stepik.org/lesson/{number}/step/1'
            browser.get(link)
            browser.implicitly_wait(10)

            try:
                WebDriverWait(browser, 1).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.navbar__activity'))
                )

            except TimeoutException:

                try:
                    login1 = WebDriverWait(browser, 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '.navbar__auth_login'))
                    )
                    login1.click()

                    email = WebDriverWait(browser, 2).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, '#id_login_email'))
                    )
                    email.send_keys(myemail)

                    password = browser.find_element(By.CSS_SELECTOR, '#id_login_password')
                    password.send_keys(mypassword)

                    login = WebDriverWait(browser, 2).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '#login_form > button'))
                    )
                    login.click()
                    time.sleep(5)# Ждем завершения авторизации
                except TimeoutException:

                    continue
            try:
                retry_button = WebDriverWait(browser, 2).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn"))
                )
                retry_button.click()

            except TimeoutException:
                print('')

            try:
                textarea = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea"))
                )
                if textarea.is_enabled():
                    answer = math.log(int(time.time()))
                    textarea.clear()
                    textarea.send_keys(str(answer))

                    button = WebDriverWait(browser, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
                    )
                    button.click()

            except TimeoutException:
                continue

            try:
                hint = WebDriverWait(browser,5).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
                )

                if hint.text != 'Correct!':
                    self.main_answer += hint.text
                    print(hint.text, end='')


            except TimeoutException:
                continue
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:

    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    y=browser.find_element(By.CSS_SELECTOR, "div  span#input_value")
    y=calc(y.text)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", input3)
    input3.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)

    browser.quit()



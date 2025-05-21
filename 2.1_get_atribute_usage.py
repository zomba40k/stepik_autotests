from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    crate = browser.find_element(By.CSS_SELECTOR, "#treasure")
    crate_get = crate.get_attribute("valuex")
    print(crate_get)
    x = calc(crate_get)
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(x)
    input3 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    input3.click()
    input2 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    input2.click()
    input4 = browser.find_element(By.CSS_SELECTOR, "button[type='Submit']")
    input4.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



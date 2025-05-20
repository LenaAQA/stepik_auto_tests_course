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
    x_elemen = browser.find_element(By.ID, "treasure")
    x_element = x_elemen.get_attribute("valuex")
    x = x_element
    y = calc(x)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    input4 = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
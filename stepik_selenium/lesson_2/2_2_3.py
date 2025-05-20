from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = int(browser.find_element(By.ID, "num1").text)
    y_element = int(browser.find_element(By.ID, "num2").text)
    answer = browser.find_element(By.ID, "dropdown").send_keys(x_element + y_element)
    browser.find_element(By.TAG_NAME, "button").click()


    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
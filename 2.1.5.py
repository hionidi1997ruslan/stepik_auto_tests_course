from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Read the vlue of variable
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = math.log(abs(12*math.sin(x)))
    input = browser.find_element(By.ID, "answer").send_keys(y)
    # set the checkbox flag
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    radiobutton = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
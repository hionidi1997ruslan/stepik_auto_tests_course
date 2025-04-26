from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Высчитываем значение
    x_element = browser.find_element(By.ID, "treasure")

    x = x_element.get_attribute("valuex")
    print(x)
    y = str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element(By.ID, "answer").send_keys(y)


    button = browser.find_element(By.ID, "robotCheckbox").click()

    button1 = browser.find_element(By.ID, "robotsRule").click()

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
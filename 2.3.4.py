from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# клик по кнопке
browser.find_element(By.XPATH, '//button[text()="I want to go on a magical journey!"]').click()
# принятие конфирма
browser.switch_to.alert.accept()

# расчет
x = browser.find_element(By.ID, "input_value").text
print(x)
y = str(math.log(abs(12*math.sin(int(x)))))

# заполнение поля 
browser.find_element(By.ID, "answer").send_keys(y)

# Нажатие на кнопку
browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

time.sleep(10)
browser.quit()
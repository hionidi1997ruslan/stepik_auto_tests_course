from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
text = WebDriverWait(browser, 15).until(
EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element(By.ID, "book").click()

# Read the vlue of variable
x = int(browser.find_element(By.ID, 'input_value').text)
y = math.log(abs(12*math.sin(x)))
input = browser.find_element(By.ID, "answer").send_keys(y)

button = browser.find_element(By.ID, "solve").click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

time.sleep(1)

# говорим Selenium проверять в течение 5 секунд, пока текст кнопки не станет "$100"
text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element(By.ID, "book")
button.click()

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
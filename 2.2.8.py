from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, '*[placeholder="Enter first name"]')
    input1.send_keys("ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '*[placeholder="Enter email"]')
    input2.send_keys("ivan@goosle.com")      
    input3 = browser.find_element(By.CSS_SELECTOR, '*[placeholder="Enter last name"]')
    input3.send_keys("koneev") 
    # Отправляем заполненную форму


    element = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
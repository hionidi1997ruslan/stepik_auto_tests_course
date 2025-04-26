from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.ID, "input_value").text
y = str(math.log(abs(12*math.sin(int(x)))))

input = browser.find_element(By.ID, "answer").send_keys(y)

radio_button = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
radio_button.click()

checkbox = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()

button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
browser.execute_script("return arguments[0].scrollIntoView(true);", button )
button .click()

time.sleep(10)
browser.quit()
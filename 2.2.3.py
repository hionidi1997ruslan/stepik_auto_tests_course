from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_el = browser.find_element(By.ID, "num1")
y_el = browser.find_element(By.ID, "num2")

x = x_el.text
y = y_el.text
sum=int(x)+int(y)

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(sum))
button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default").click()

time.sleep(10)
browser.quit()
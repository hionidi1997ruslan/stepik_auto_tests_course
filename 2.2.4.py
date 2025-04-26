import time
from selenium import webdriver

browser = webdriver.Chrome() # open the browser

browser.execute_script("document.title='Script executing';alert('Robots at work');") # changetittle

time.sleep(10)
browser.quit()
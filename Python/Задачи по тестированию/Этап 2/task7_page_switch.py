from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

button = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')
button.click()

first_tab = browser.window_handles[0]
second_tab = browser.window_handles[1]
browser.switch_to.window(second_tab)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = int(x_element.text)
y = math.log(abs(12*math.sin(x)))

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(y)

submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
submit.click()
time.sleep(2)

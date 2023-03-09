from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit.click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = int(x_element.text)
y = math.log(abs(12*math.sin(x)))

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(y)

submit2 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
submit2.click()
time.sleep(5)

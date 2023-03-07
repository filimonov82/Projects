from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('https://SunInJuly.github.io/execute_script.html')
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = int(x_element.text)
y = math.log(abs(12*math.sin(x)))

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
checkbox.click()

radiobutton = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
browser.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
radiobutton.click()

submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
submit.click()
time.sleep(5)

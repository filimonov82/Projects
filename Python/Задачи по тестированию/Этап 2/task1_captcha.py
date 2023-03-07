from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

page = browser.get('https://suninjuly.github.io/math.html')

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text  # обращение к тексту тега
y = calc(x)

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(y)

checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
checkbox.click()

radiobox = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
radiobox.click()

submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
submit.click()
time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button_book = browser.find_element(By.CSS_SELECTOR, '#book')
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100')
)
button_book.click()

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = int(x_element.text)
y = math.log(abs(12*math.sin(x)))

answer = browser.find_element(By.CSS_SELECTOR, '#answer')
answer.send_keys(y)
browser.execute_script("return arguments[0].scrollIntoView('true');", answer)  # не обязательно прокручивать, но кнопка была еле видна

submit = browser.find_element(By.CSS_SELECTOR, '#solve')
submit.click()
time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/selects1.html')
num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
total = int(num1) + int(num2)

dropdown = browser.find_element(By.CSS_SELECTOR, '#dropdown')
dropdown.click()

dropdown_list = browser.find_elements(By.CSS_SELECTOR, '#dropdown option')
for option in dropdown_list:
    if option.text == str(total):
        option.click()
        break

submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
submit.click()
time.sleep(5)

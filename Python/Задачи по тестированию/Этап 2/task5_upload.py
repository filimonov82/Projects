from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
name.send_keys('Name')
surname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
surname.send_keys('Surname')
email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
email.send_keys('Email')

file = browser.find_element(By.CSS_SELECTOR, '#file')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'task5_upload.txt')
file.send_keys(file_path)

submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
submit.click()
time.sleep(5)

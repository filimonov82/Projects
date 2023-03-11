from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestSite(unittest.TestCase):
    def test_site1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        placeholder1 = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
        placeholder2 = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
        placeholder3 = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
        placeholder1.send_keys('Value')
        placeholder2.send_keys('Value')
        placeholder3.send_keys('Value')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")

    def test_site2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        placeholder1 = browser.find_element(By.CSS_SELECTOR, '.first_block input.first')
        placeholder2 = browser.find_element(By.CSS_SELECTOR, '.first_block input.second')
        placeholder3 = browser.find_element(By.CSS_SELECTOR, '.first_block input.third')
        placeholder1.send_keys('Value')
        placeholder2.send_keys('Value')
        placeholder3.send_keys('Value')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

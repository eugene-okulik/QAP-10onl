from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def check_checkbox(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    checkbox = driver.find_element(By.ID, 'isAgeSelected')
    checkbox.click()
    checkbox_text = driver.find_element(By.ID, 'txtAge')
    print(checkbox_text.text)
    driver.quit()


driver = open_browser()
check_checkbox(driver)

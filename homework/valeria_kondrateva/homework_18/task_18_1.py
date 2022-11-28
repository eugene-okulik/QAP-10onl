from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def find_by_id(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    checkbox = driver.find_element(By.ID, 'isAgeSelected')
    checkbox.click()
    show_text = driver.find_element(By.ID, 'txtAge')
    print(show_text.text)


common_driver = open_browser()
find_by_id(common_driver)
common_driver.quit()

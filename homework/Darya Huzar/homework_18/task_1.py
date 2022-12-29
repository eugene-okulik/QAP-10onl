from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    sleep(2)
    return chrome_driver


def single_checkbox_demo(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    checkbox_element = driver.find_element(By.ID, 'isAgeSelected')
    sleep(2)
    checkbox_element.click()
    sleep(2)
    checkbox_element_after_click = driver.find_element(By.ID, 'txtAge')
    print(checkbox_element_after_click.text)


common_driver = open_browser()
single_checkbox_demo(common_driver)
common_driver.quit()

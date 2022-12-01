from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def single_checkbox(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    single_checkbox_demo = driver.find_element(By.ID, 'isAgeSelected')
    single_checkbox_demo.click()
    single_checkbox_demo_text = driver.find_element(By.ID, 'txtAge')
    print(single_checkbox_demo_text.text)


common_driver = open_browser()
single_checkbox(common_driver)
sleep(3)
common_driver.quit()

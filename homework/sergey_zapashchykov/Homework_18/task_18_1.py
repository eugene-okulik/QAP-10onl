from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def checkbox_usage(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    check_box_button = driver.find_element(By.ID, 'isAgeSelected')
    check_box_button.click()
    check_box_button_click_text = driver.find_element(By.ID, 'txtAge')
    print(check_box_button_click_text.text)


common_driver = open_browser()
checkbox_usage(common_driver)
sleep(1.5)
common_driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def checkboxes_usage(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    check_all_button = driver.find_element(By.ID, 'check1')
    check_all_button.click()
    check_box_button = driver.find_element(By.CLASS_NAME, 'cb1-element')
    check_box_button.click()
    check_box_button_value = check_all_button.get_attribute('value')
    print(check_box_button_value)


common_driver = open_browser()
checkboxes_usage(common_driver)
sleep(1.5)
common_driver.quit()

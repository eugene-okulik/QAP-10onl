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


def multiple_checkbox_demo(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    check_all_button = driver.find_element(By.ID, 'check1')
    sleep(2)
    check_all_button.click()
    sleep(2)
    check_box_1 = driver.find_element(By.CLASS_NAME, 'cb1-element')
    sleep(2)
    check_box_1.click()
    sleep(2)
    class_attribute = check_all_button.get_attribute('value')
    print(class_attribute)


common_driver = open_browser()
multiple_checkbox_demo(common_driver)
common_driver.quit()

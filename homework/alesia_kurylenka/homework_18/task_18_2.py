from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def find_multiple_checkbox_by_id(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    check_all_button = driver.find_element(By.ID, 'check1')
    check_all_button.click()
    choose_one_checkbox = driver.find_element(By.CLASS_NAME, 'cb1-element')
    choose_one_checkbox.click()
    check_button_text = check_all_button.get_attribute('value')
    print(check_button_text)


common_driver = open_browser()
find_multiple_checkbox_by_id(common_driver)
common_driver.quit()

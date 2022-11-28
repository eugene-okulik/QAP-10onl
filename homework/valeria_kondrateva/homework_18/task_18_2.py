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
    mult_checkbox = driver.find_element(By.ID, 'check1')
    mult_checkbox.click()


def find_by_class_and_get_attribute(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    option_1 = driver.find_element(By.CLASS_NAME, 'cb1-element')
    option_1.click()
    opt_1 = option_1.get_attribute('class')
    print(opt_1)


common_driver = open_browser()
find_by_class_and_get_attribute(common_driver)
common_driver.quit()

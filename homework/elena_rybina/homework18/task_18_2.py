from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def check_checkbox_all(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    checkbox_all = driver.find_element(By.ID, 'check1')
    checkbox_all.click()
    checkbox_3 = driver.find_elements(By.CLASS_NAME, 'cb1-element')
    checkbox_3[2].click()
    checkbox_all_text = checkbox_all.get_attribute('value')
    print(checkbox_all_text)
    driver.quit()


driver = open_browser()
check_checkbox_all(driver)

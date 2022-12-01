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


def multiple_checkbox(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    multiple_checkbox_demo = driver.find_element(By.ID, 'check1')
    multiple_checkbox_demo.click()
    option_3 = driver.find_element(By.CSS_SELECTOR, '#easycont > div > div.col-md-6.text-left > div:nth-child(5) > '
                                                    'div.panel-body > div:nth-child(5) > label > input')
    option_3.click()
    multiple_checkbox_text = multiple_checkbox_demo.get_attribute('value')
    print(multiple_checkbox_text)


common_driver = open_browser()
multiple_checkbox(common_driver)
sleep(3)
common_driver.quit()

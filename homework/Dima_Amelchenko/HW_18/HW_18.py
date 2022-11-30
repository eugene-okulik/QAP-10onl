from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver_chrome = webdriver.Chrome(options=options)
    driver_chrome.implicitly_wait(10)
    return driver_chrome


def test_check_box(driver_chrome):
    driver_chrome.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')

    single_checkbox_demo = driver_chrome.find_element(By.ID, 'isAgeSelected')
    single_checkbox_demo.click()

    text_single_checkbox_demo = driver_chrome.find_element(By.ID, 'txtAge').text
    print(text_single_checkbox_demo)

    all_check_box = driver_chrome.find_element(By.ID, 'check1')
    all_check_box.click()

    option_3 = driver_chrome.find_elements(By.CLASS_NAME, 'cb1-element')
    option_3[2].click()

    text_all_check_box = all_check_box.get_attribute('value')
    print(text_all_check_box)


driver_chrome = driver()
test_check_box(driver_chrome)
driver_chrome.quit()

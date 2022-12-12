from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
check_all_btn = chrome_driver.find_element(By.CSS_SELECTOR, '.btn-primary')
check_all_btn.click()
check_boxes = chrome_driver.find_elements(By.CSS_SELECTOR, '.cb1-element')
check_boxes[1].click()
print(check_all_btn.get_attribute('value'))

chrome_driver.quit()

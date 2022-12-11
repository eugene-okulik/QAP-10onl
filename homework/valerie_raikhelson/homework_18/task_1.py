from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
chrome_driver.find_element(By.ID, 'isAgeSelected').click()
print(chrome_driver.find_element(By.ID, 'txtAge').text)
chrome_driver.quit()
chrome_driver.close()

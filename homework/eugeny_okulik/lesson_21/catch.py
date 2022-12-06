from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
sleep(3)
driver.implicitly_wait(10)
driver.get('https://demoqa.com/automation-practice-form')
input_ = driver.find_element(By.ID, 'subjectsInput')
input_.send_keys('ph')
elt = driver.find_element(By.CLASS_NAME, 'css-26l3qy-menu')
print(elt.get_attribute('innerHTML'))
driver.find_element(By.ID, 'react-select-2-option-0').click()
sleep(5)

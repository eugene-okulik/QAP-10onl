from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import random


def open_browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def click_multiple_chb(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    checkbox_button = driver.find_element(By.ID, "check1")
    checkbox_button.click()
    random_checkbox = driver.find_elements(By.CLASS_NAME, "cb1-element")
    random_checkbox[random.choice([1, 2, 3, 0])].click()
    print(checkbox_button.get_attribute("value"))


driver = open_browser()
click_multiple_chb(driver)
sleep(2)
driver.quit()

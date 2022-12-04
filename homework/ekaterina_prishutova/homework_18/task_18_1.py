from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def open_browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def click_single_chb(driver):
    driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
    checkbox = driver.find_element(By.ID, "isAgeSelected")
    checkbox.click()
    text_chb = driver.find_element(By.ID, "txtAge")
    print(text_chb.get_attribute("innerText"))


driver = open_browser()
click_single_chb(driver)
sleep(2)
driver.quit()

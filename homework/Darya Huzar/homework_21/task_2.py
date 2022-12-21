from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def open_chrome():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def tools_qa(driver):
    driver.get('https://demoqa.com/menu#')
    main_item_2 = driver.find_element(By.XPATH, '//a[text() = "Main Item 2"]')
    sub_sub_list = driver.find_element(By.XPATH, '//a[text() = "SUB SUB LIST »"]')
    sub_sub_item_2 = driver.find_element(By.XPATH, '//a[text() = "Sub Sub Item 2"]')
    ActionChains(driver).move_to_element(main_item_2).move_to_element(sub_sub_list).move_to_element(
        sub_sub_item_2).perform()
    sleep(1)
    print(f"Clicked: {sub_sub_item_2.text}.")


driver = open_chrome()
tools_qa(driver)
driver.quit()

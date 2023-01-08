from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


def open_chrome():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def alert_box(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    prompt_box = driver.find_element(By.ID, 'promptexample')
    prompt_box.click()
    Alert(driver).send_keys("Hello, world")
    Alert(driver).accept()
    sleep(5)
    prompt_text = driver.find_element(By.ID, 'promptreturn')
    assert "Hello, world" in prompt_text.text


driver = open_chrome()
alert_box(driver)
driver.quit()

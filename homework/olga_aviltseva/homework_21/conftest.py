from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    return chrome_driver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from time import sleep


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    sleep(3)
    yield chrome_driver
    chrome_driver.quit()

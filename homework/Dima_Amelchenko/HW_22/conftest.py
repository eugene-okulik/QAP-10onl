from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver_crome = webdriver.Chrome(options=options)
    driver_crome.implicitly_wait(10)
    return driver_crome

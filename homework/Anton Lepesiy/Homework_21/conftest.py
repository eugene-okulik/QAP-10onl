from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", False)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(3)
    return chrome_driver

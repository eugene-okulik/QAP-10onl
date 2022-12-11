from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('window-size=1024,768')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(3)
    return chrome_driver

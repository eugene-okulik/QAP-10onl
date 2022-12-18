from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_argument('window-size=1024,768')
    chrome_driver = webdriver.Chrome(options=options)
    # chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    # chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()

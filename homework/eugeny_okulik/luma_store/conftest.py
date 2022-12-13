from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.whats_new_page import WhatsNewPage
import pytest


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    # chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def whats_new(driver):
    whats_new_page = WhatsNewPage(driver)
    whats_new_page.open()
    return whats_new_page

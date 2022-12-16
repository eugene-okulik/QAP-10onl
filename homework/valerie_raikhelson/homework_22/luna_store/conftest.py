from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_account import CreateAccountPage
from pages.eco_friendly import EcoFriendlyPage
from pages.sale import SalePage
import pytest


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(10)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(scope='function')
def create_account(driver):
    create_account = CreateAccountPage(driver)
    create_account.open()
    return create_account


@pytest.fixture(scope='function')
def eco_friendly(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()
    return eco_friendly


@pytest.fixture(scope='function')
def sale(driver):
    sale = SalePage(driver)
    sale.open()
    return sale

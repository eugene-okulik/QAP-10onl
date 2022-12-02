from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def prepare():
    print('before')
    yield
    print('after')


@pytest.fixture(scope='function')
def driver():
    # print('Before driver')
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('window-size=1000,600')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    # print('after driver')
    chrome_driver.quit()


@pytest.fixture(scope='session')
def when():
    print('Before')
    yield
    print('After')


@pytest.mark.smoke
def test_one(when):
    # print(prepare)
    assert 2 == 2


@pytest.mark.slow
def test_two():
    print('I am test two', end='')
    assert 1 == 1, 'One is not one'


def test_three(when):
    assert 3 == 3


@pytest.mark.skipif(datetime.now().year == 2022, reason='Not supported in 2022')
def test_four():
    assert 4 == 4


@pytest.mark.skip('Slow UI test')
def test_tabs(driver):
    driver.get('https://the-internet.herokuapp.com/windows')
    link = driver.find_element(By.LINK_TEXT, 'Click Here')
    link.click()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'New Window', 'Page has wrong text'
    driver.switch_to.window(driver.window_handles[0])
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Opening a new window'


CREDS = [
    ('user1', '3984734'),
    ('user2', '0476456'),
    ('user3', '458974958')
]


@pytest.mark.parametrize('creds', CREDS)
def test_login(driver, creds):
    driver.get('https://demoblaze.com/')
    driver.find_element(By.ID, 'login2').click()
    login = driver.find_element(By.ID, 'loginusername')
    passwd = driver.find_element(By.ID, 'loginpassword')
    button = driver.find_element(By.XPATH, '//button[@onclick="logIn()"]')
    log, pas = creds
    login.send_keys(log)
    passwd.send_keys(pas)
    button.click()
    assert 'Login is successful'

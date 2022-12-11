from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

URL = 'https://testpages.herokuapp.com/styled/alerts/alert-test.html'


def test_alert(driver):
    driver.get(URL)
    driver.find_element(By.CSS_SELECTOR, '#promptexample').click()
    text = 'hello'
    Alert(driver).send_keys(text)
    Alert(driver).accept()
    assert text in driver.find_element(By.CSS_SELECTOR, '#promptreturn').text

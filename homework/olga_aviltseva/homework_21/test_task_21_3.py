from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_alert(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, 'promptexample').click()
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.send_keys("test")
    alert.accept()
    assert driver.find_element(By.ID, 'promptreturn').text == "test"

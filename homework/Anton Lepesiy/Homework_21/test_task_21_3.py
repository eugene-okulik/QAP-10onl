from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


URL = 'https://testpages.herokuapp.com/styled/alerts/alert-test.html'
user_text = 'Мама - Анархія'


def test_to_alert_send_text(driver):
    driver.get(URL)
    prompt_button = driver.find_element(By.ID, 'promptexample')
    showed_text = driver.find_element(By.ID, 'promptreturn')
    alert = Alert(driver)

    prompt_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.send_keys(user_text)
    alert.accept()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    assert showed_text.text == user_text

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_alerts(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    show_prompt_box = driver.find_element(By.ID, 'promptexample')
    show_prompt_box.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.send_keys("I accept this alert!")
    alert.accept()
    hello_text = driver.find_element(By.ID, 'promptreturn')
    assert hello_text.text == "I accept this alert!"

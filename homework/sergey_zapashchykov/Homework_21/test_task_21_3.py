from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def test_alert_box(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    show_prompt_box = driver.find_element(By.ID, 'promptexample')
    show_prompt_box.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.send_keys('Sample text')
    alert.accept()
    show_prompt_box_return = driver.find_element(By.XPATH, '//span[@id="promptretval"]')
    assert show_prompt_box_return.text == 'Sample text'

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_three(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    show_prompt_box_button = driver.find_element(By.ID, 'promptexample')
    show_prompt_box_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.send_keys('blah blah blah')
    alert.accept()
    prompt_return = driver.find_element(By.XPATH, '//div[@class="centered"][3]/p[1]')
    assert prompt_return.text == 'blah blah blah'

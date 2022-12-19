from selenium.webdriver.support import expected_conditions as EC


def test_three(driver):
    driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    show_prompt_box = driver.find_element(By.ID, 'promptexample')
    show_prompt_box.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.send_keys("Guten Tag!")
    alert.accept()
    msg = driver.find_element(By.ID, 'promptreturn')
    assert msg.text == "Guten tag!"

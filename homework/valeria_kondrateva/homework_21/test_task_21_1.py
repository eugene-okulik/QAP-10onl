from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product = driver.find_element(By.XPATH, '//a[@href="prod.html?idp_=1"]')
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH, '//a[@onclick="addToCart(2)"]').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, 'cartur').click()
    assert driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]').text == 'Samsung galaxy s6'

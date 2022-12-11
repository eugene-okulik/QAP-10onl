from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product = driver.find_element(By.XPATH, '//a[@href="prod.html?idp_=2"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(product)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    driver.switch_to.window(driver.window_handles[1])
    add_to_cart = driver.find_element(By.XPATH, '//a[@onclick="addToCart(2)"]')
    add_to_cart.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    in_cart = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert in_cart.text == 'Nokia lumia 1520'

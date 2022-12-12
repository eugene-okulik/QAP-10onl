from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def test_add_product(driver):
    driver.get('https://www.demoblaze.com/index.html')
    product = driver.find_element(By.XPATH, '//a[@href="prod.html?idp_=1"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(product)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    driver.switch_to.window(driver.window_handles[1])
    add_to_card = driver.find_element(By.XPATH, '//a[@onclick="addToCart(1)"]')
    add_to_card.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    product_in_cart = driver.find_element(By.XPATH, '//tr[@class="success"]//td[2]')
    assert product_in_cart.text == 'Samsung galaxy s6'

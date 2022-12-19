from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


def test_one(driver):
    driver.get('https://www.demoblaze.com/index.html')
    lumia = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//a[@href=\"prod.html?idp_=2\"])[2]")))
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(lumia)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    driver.switch_to.window(driver.window_handles[1])
    lumia_add_to_card_button = driver.find_element(By.XPATH, '//a[@onclick="addToCart(2)"]')
    lumia_add_to_card_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    cart_with_lumia = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert cart_with_lumia.text == 'Nokia lumia 1520'

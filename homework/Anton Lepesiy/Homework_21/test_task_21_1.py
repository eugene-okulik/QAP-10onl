from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


URL = 'https://www.demoblaze.com/index.html'
selected_item = 'Nexus 6'


def test_add_item_to_cart(driver):
    driver.get(URL)
    item = driver.find_element(By.LINK_TEXT, selected_item)
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL)
    action.click(item)
    action.key_up(Keys.CONTROL)
    action.perform()
    driver.switch_to.window(driver.window_handles[1])
    add_button = driver.find_element(By.LINK_TEXT, 'Add to cart')
    add_button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, 'cartur').click()
    item_in_cart = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert item_in_cart.text == selected_item

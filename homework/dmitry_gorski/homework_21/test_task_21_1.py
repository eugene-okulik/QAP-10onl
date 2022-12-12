from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = 'https://www.demoblaze.com/index.html'


def test_one(driver):
    driver.get(link)
    phone = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    ActionChains(driver).key_down(Keys.CONTROL).click(phone).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element(By.ID, 'cartur').click()
    phone_in_basket = driver.find_element(By.XPATH, '//tr[@class="success"]/td[2]')
    assert 'Samsung galaxy s6' == phone_in_basket.text

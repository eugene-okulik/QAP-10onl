from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def open_chrome():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def add_item(driver):
    driver.get('https://www.demoblaze.com/index.html')
    item = driver.find_element(By.LINK_TEXT, 'Nokia lumia 1520')
    ActionChains(driver).key_down(Keys.CONTROL).click(item).key_up(Keys.CONTROL).perform()
    driver.switch_to.window(driver.window_handles[1])
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'a[onclick="addToCart(2)"]')
    add_to_cart_button.click()
    WebDriverWait(driver, 10).until(ec.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    cart_button = driver.find_element(By.ID, 'cartur')
    cart_button.click()
    added_item = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    assert 'Nokia lumia 1520' in added_item.text


driver = open_chrome()
add_item(driver)
driver.quit()

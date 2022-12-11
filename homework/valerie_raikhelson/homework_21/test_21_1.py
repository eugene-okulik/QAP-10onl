from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://www.demoblaze.com/index.html'


def open_page_in_new_tab(driver, element):
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()


def switch_tab(driver, tab):
    driver.switch_to.window(driver.window_handles[tab])


def click(driver, path):
    element = driver.find_element(By.CSS_SELECTOR, path)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))
    element.click()


def accept_alert(driver):
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    Alert(driver).accept()


def close_tab(driver):
    driver.close()


def test_phone_purchase(driver):
    driver.get(URL)
    mobile_phone = driver.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    open_page_in_new_tab(driver, mobile_phone)
    switch_tab(driver, 1)
    selected_phone = driver.find_element(By.CSS_SELECTOR, '#tbodyid>h2').text
    click(driver, '.btn-lg')
    accept_alert(driver)
    close_tab(driver)
    switch_tab(driver, 0)
    click(driver, '#cartur')
    details_of_selected_phone = driver.find_element(By.CSS_SELECTOR, ".success>:nth-child(2)")
    assert selected_phone == details_of_selected_phone.text

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('window-size=1000,600')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    # by_css_sel(chrome_driver)
    sleep(3)
    # chrome_driver.maximize_window()
    return chrome_driver


def by_link_text(driver):
    driver.get('https://www.google.com/')
    mail = driver.find_element(By.LINK_TEXT, 'Gmail')
    # mail = driver.find_element(By.PARTIAL_LINK_TEXT, 'Gma')
    mail.click()


def by_css_sel(driver):
    driver.get('https://www.saucedemo.com/')
    login_button = driver.find_element(By.CSS_SELECTOR, '.submit-button, .bot_column')  # By class name:first or second
    login_button = driver.find_element(By.CSS_SELECTOR, '.submit-button.btn_action')  # By two class names
    # login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')  # By id
    # login_button = driver.find_element(By.CSS_SELECTOR, 'input[data-test="login-button"]')  # By attribute value
    login_field = driver.find_element(By.CSS_SELECTOR, '.input_error.form_input[placeholder="Username"]')
    passw_field = driver.find_element(By.CSS_SELECTOR, '.input_error.form_input[placeholder="Password"]')
    login_field.send_keys('standard_user')
    passw_field.send_keys('secret_sauce')
    login_button.click()


def by_xpath(driver):
    driver.get('https://www.saucedemo.com/')
    # login_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login_field = driver.find_element(By.XPATH, '//input[@class="input_error form_input" and @placeholder="Username"]')
    passw_field = driver.find_element(By.XPATH, '//input[@class="input_error form_input" and @placeholder="Password"]')
    login_button = driver.find_element(By.XPATH, '//input[@class="submit-button btn_action"]')
    login_field.send_keys('standard_user')
    sleep(1)
    login_field.clear()
    sleep(3)
    passw_field.send_keys('secret_sauce')
    sleep(2)
    login_button.click()


def actions(driver):
    driver.get('https://www.saucedemo.com/')
    login_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    print(login_field.get_attribute('autocorrect'))
    logins = driver.find_element(By.ID, 'login_credentials')
    print(logins.get_attribute('innerText'))
    print(logins.text)
    login_button = driver.find_element(By.XPATH, '//input[@class="submit-button btn_action"]')
    print(login_button.value_of_css_property('background-color'))
    print(login_button.tag_name)


def checkboxes(driver):
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    form = driver.find_element(By.ID, 'checkboxes').is_displayed()
    print(form.is_displayed())
    checkboxes_2 = form.find_elements(By.TAG_NAME, 'input')
    print(checkboxes_2[0].is_selected())
    for checkbox in checkboxes_2:
        checkbox.click()
    # Wait until the element checkboxes_2[0] is selected:
    WebDriverWait(driver, 10).until(EC.element_to_be_selected(checkboxes_2[0]))
    print(checkboxes_2[0].is_selected())


def selects(driver):
    driver.get('https://demo.seleniumeasy.com/basic-select-dropdown-demo.html')
    select = driver.find_element(By.ID, 'select-demo')
    dropdown = Select(select)
    dropdown.select_by_value('Sunday')
    dropdown.select_by_visible_text('Tuesday')


def tabs(driver):
    driver.get('https://the-internet.herokuapp.com/windows')
    link = driver.find_element(By.LINK_TEXT, 'Click Here')
    link.click()
    driver.switch_to.window(driver.window_handles[1])
    print(driver.find_element(By.TAG_NAME, 'h3').text)
    driver.switch_to.window(driver.window_handles[0])
    print(driver.find_element(By.TAG_NAME, 'h3').text)


def cookies(driver):
    driver.get('https://demoblaze.com/')
    driver.add_cookie({'name': 'test', 'value': 'bar'})
    print(driver.get_cookies())


common_driver = open_browser()
cookies(common_driver)
sleep(3)
common_driver.quit()

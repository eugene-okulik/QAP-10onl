from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('window-size=100,1600')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def form_filler(browser):
    browser.get('https://demoqa.com/automation-practice-form')
    first_name = browser.find_element(By.ID, 'firstName')
    first_name.send_keys('Vasiliy')
    last_name = browser.find_element(By.ID, 'lastName')
    last_name.send_keys('Testovsky')
    first_name = browser.find_element(By.ID, 'userEmail')
    first_name.send_keys('supertest@google.com')
    gender = browser.find_elements(By.CSS_SELECTOR, '.custom-control, .custom-radio, .custom-control-inline')
    gender[1].click()
    phone = browser.find_element(By.ID, 'userNumber')
    phone.send_keys('1212111111')
    subject = browser.find_element(By.ID, 'subjectsInput')
    subject.send_keys('English')
    subject.send_keys(Keys.ENTER)
    birth = browser.find_element(By.ID, 'dateOfBirthInput')
    birth.click()
    month = Select(browser.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    month.select_by_index(4)
    year = Select(browser.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    year.select_by_index(87)
    day = browser.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--003')
    day.click()
    hobbies = browser.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    hobbies.click()
    adress_placeholder = browser.find_element(By.ID, 'currentAddress')
    adress_placeholder.send_keys('City, Street-1, House-12, Flat-333')
    state = browser.find_element(By.ID, 'state')
    state.click()
    state_input = browser.find_element(By.ID, 'react-select-3-input')
    state_input.send_keys('NCR')
    state_input.send_keys(Keys.ENTER)
    city = browser.find_element(By.ID, 'city')
    city.click()
    city_input = browser.find_element(By.ID, 'react-select-4-input')
    city_input.send_keys('Delhi')
    city_input.send_keys(Keys.ENTER)
    submit = browser.find_element(By.ID, 'submit')
    submit.click()


browser = open_browser()
form_filler(browser)

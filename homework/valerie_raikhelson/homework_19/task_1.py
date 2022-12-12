from selenium.webdriver import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def open_browser():
    options = Options()
    options.add_argument('window-size=700,700')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def open_page(driver):
    driver.get('https://demoqa.com/automation-practice-form')


def close_driver(driver):
    driver.close()
    driver.quit()


def find_element(driver, path):
    return driver.find_element(By.CSS_SELECTOR, path)


def select_by_value(element, value):
    dropdown = Select(element)
    dropdown.select_by_value(value)


def student_reg_form(driver):
    first_name = find_element(driver, '#firstName')
    first_name.send_keys('Valerie')
    last_name = find_element(driver, '#lastName')
    last_name.send_keys('Raikhelson')
    email = find_element(driver, '#userEmail')
    email.send_keys('val@an.com')
    gender_female = find_element(driver, "[for='gender-radio-2']")
    gender_female.click()
    mobile_number = find_element(driver, '#userNumber')
    mobile_number.send_keys('0543908912')
    date_of_birth = find_element(driver, '#dateOfBirthInput')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    date_of_birth.click()
    select_month = find_element(driver, '.react-datepicker__month-select')
    select_by_value(select_month, '11')
    select_year = find_element(driver, '.react-datepicker__year-select')
    select_by_value(select_year, '1993')
    choose_day = find_element(driver, '.react-datepicker__day--009')
    choose_day.click()
    hobby_sports = find_element(driver, "[for='hobbies-checkbox-1']")
    hobby_sports.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    upload_picture = find_element(driver, '#uploadPicture')
    upload_picture.send_keys('C:/Users/Valerie/Desktop/katy.jpg')
    current_address = find_element(driver, '#currentAddress')
    current_address.send_keys('Test address')
    state = driver.find_element(By.ID, 'state')
    state.click()
    select_state = find_element(driver, '#react-select-3-input')
    select_state.send_keys('NCR')
    select_state.send_keys(Keys.ENTER)
    city = driver.find_element(By.ID, 'city')
    city.click()
    select_city = find_element(driver, '#react-select-4-input')
    select_city.send_keys('Delhi')
    select_city.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    submit = find_element(driver, '#submit')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit))
    submit.click()
    sleep(5)
    content = find_element(driver, '.modal-content')
    print(content.text)


chrome_driver = open_browser()
open_page(chrome_driver)
student_reg_form(chrome_driver)
close_driver(chrome_driver)

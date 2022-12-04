import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = 'https://demoqa.com/automation-practice-form'


def open_browser():
    web_driver = webdriver.Chrome()
    web_driver.implicitly_wait(10)
    return web_driver


def student_form(driver):
    driver.get(link)

    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Dmitry')

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Gorski')

    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('dhorski@gmail.com')

    gender = driver.find_elements(By.CSS_SELECTOR, '.custom-control, .custom-radio, .custom-control-inline')
    gender[0].click()

    phone = driver.find_element(By.ID, 'userNumber')
    phone.send_keys('0123456789')

    birth = driver.find_element(By.ID, 'dateOfBirthInput')
    birth.click()

    birth_month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    birth_month_sel = Select(birth_month)
    birth_month_sel.select_by_index(8)

    birth_year = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    birth_year_sel = Select(birth_year)
    birth_year_sel.select_by_visible_text('1982')

    birth_day = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--003')
    birth_day.click()

    subjects = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subjects.click()
    subjects.send_keys('Maths')
    subjects.send_keys(Keys.ENTER)

    hobbies = driver.find_elements(By.CSS_SELECTOR, '.custom-control.custom-checkbox.custom-control-inline')
    hobbies[0].click()

    attach_file = driver.find_element(By.ID, 'uploadPicture')
    attach_file.send_keys(os.path.join('d:/', 'QA_python.jpg'))

    address = driver.find_element(By.ID, 'currentAddress')
    address.send_keys('Belarus, Minsk')

    state_window = driver.find_element(By.ID, 'state')
    state = state_window.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
    state.send_keys('NCR')
    state.send_keys(Keys.ENTER)

    city_window = driver.find_element(By.ID, 'city')
    city = city_window.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
    city.send_keys('Delhi')
    city.send_keys(Keys.ENTER)

    submit = driver.find_element(By.ID, 'submit')
    submit.submit()

    modal_window = driver.find_element(By.CLASS_NAME, 'modal-content')
    print(modal_window.text)


chrome_driver = open_browser()
student_form(chrome_driver)
chrome_driver.quit()

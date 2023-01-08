from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def open_chrome():
    options = Options()
    options.add_argument("start-maximized")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def practice_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name_field = driver.find_element(By.ID, 'firstName')
    first_name_field.send_keys('Darya')
    sleep(1)
    last_name_field = driver.find_element(By.ID, 'lastName')
    last_name_field.send_keys('Huzar')
    sleep(1)
    email_field = driver.find_element(By.ID, 'userEmail')
    email_field.send_keys("notarealemail@gmail.com")
    sleep(1)
    gender_choice = driver.find_element(By.XPATH, '//label[@for="gender-radio-2"]')
    gender_choice.click()
    sleep(1)
    mobile_field = driver.find_element(By.ID, 'userNumber')
    mobile_field.send_keys('5251234567')
    sleep(1)
    date_of_birth_field = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth_field.click()
    sleep(0.5)
    select_month_field = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    select_month_field.select_by_visible_text('June')
    sleep(0.5)
    select_year_field = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    select_year_field.select_by_value('1994')
    sleep(0.5)
    select_day_field = driver.find_element(By.XPATH, '//div[@class="react-datepicker__month"]/div[3]/div[3]')
    select_day_field.click()
    sleep(1)
    subjects_field = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subjects_field.send_keys('E')
    subjects_field_list = driver.find_element(By.ID, 'react-select-2-option-0')
    subjects_field_list.click()
    sleep(1)
    hobbies_choice = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    hobbies_choice.click()
    sleep(1)
    current_address_field = driver.find_element(By.ID, 'currentAddress')
    current_address_field.send_keys('Minsk, Belarus')
    sleep(0.5)
    driver.execute_script("document.body.style.zoom = '0.8'")
    sleep(0.5)
    state_field = driver.find_element(By.ID, 'react-select-3-input')
    state_field.send_keys('NCR')
    state_field.send_keys(Keys.ENTER)
    sleep(1)
    city_field = driver.find_element(By.ID, 'react-select-4-input')
    city_field.send_keys('Delhi')
    city_field.send_keys(Keys.ENTER)
    sleep(0.5)
    submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit.submit()
    sleep(5)


driver = open_chrome()
practice_form(driver)
driver.quit()

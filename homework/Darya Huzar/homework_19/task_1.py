from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
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
    last_name_field = driver.find_element(By.ID, 'lastName')
    last_name_field.send_keys('Huzar')
    email_field = driver.find_element(By.ID, 'userEmail')
    email_field.send_keys("notarealemail@gmail.com")
    gender_choice = driver.find_element(By.XPATH, '//label[@for="gender-radio-2"]')
    gender_choice.click()
    mobile_field = driver.find_element(By.ID, 'userNumber')
    mobile_field.send_keys('5251234567')
    date_of_birth_field = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth_field.click()
    select_month_field = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select'))
    select_month_field.select_by_visible_text('June')
    select_year_field = Select(driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select'))
    select_year_field.select_by_value('1994')
    select_day_field = driver.find_element(By.XPATH, '//div[@class="react-datepicker__month"]/div[3]/div[3]')
    select_day_field.click()
    subjects_field = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subjects_field.send_keys('E')
    subjects_field_list = driver.find_element(By.ID, 'react-select-2-option-0')
    subjects_field_list.click()
    hobbies_choice = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    hobbies_choice.click()
    current_address_field = driver.find_element(By.ID, 'currentAddress')
    current_address_field.send_keys('Minsk, Belarus')
    driver.execute_script("document.body.style.zoom = '0.8'")
    state_field = driver.find_element(By.ID, 'react-select-3-input')
    state_field.send_keys('NCR')
    state_field.send_keys(Keys.ENTER)
    city_field = driver.find_element(By.ID, 'react-select-4-input')
    city_field.send_keys('Delhi')
    city_field.send_keys(Keys.ENTER)
    submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit.submit()


driver = open_chrome()
practice_form(driver)
driver.quit()

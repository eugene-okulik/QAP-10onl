from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def open_browser():
    options = Options()
    options.add_argument('window-size=700,1500')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def fill_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name_field = driver.find_element(By.ID, 'firstName')
    first_name_field.send_keys('Olga')
    last_name_field = driver.find_element(By.ID, 'lastName')
    last_name_field.send_keys('Aviltseva')
    email_field = driver.find_element(By.ID, 'userEmail')
    email_field.send_keys('Olgaaviltseva@gmail.com')
    gender_field = driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-2"]')
    gender_field.click()
    mobile_number_field = driver.find_element(By.ID, 'userNumber')
    mobile_number_field.send_keys('1234567890')
    date_birth_field = driver.find_element(By.ID, 'dateOfBirthInput')
    date_birth_field.click()
    year_birth = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    dropdown_year = Select(year_birth)
    dropdown_year.select_by_value('2000')
    month_birth = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    dropdown_month = Select(month_birth)
    dropdown_month.select_by_value('5')
    day_birth = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Choose Sunday, June 4th, 2000"]')
    day_birth.click()
    subjects_field = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subjects_field.click()
    subjects_field.send_keys('Physics')
    subjects_field.send_keys(Keys.ENTER)
    hobbies_field = driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]')
    hobbies_field.click()
    address_field = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    address_field.send_keys('Test Adress')
    state_field = driver.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
    state_field.send_keys('Uttar Pradesh')
    state_field.send_keys(Keys.ENTER)
    city_field = driver.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
    city_field.send_keys('Merrut')
    city_field.send_keys(Keys.ENTER)
    state_field.submit()


common_driver = open_browser()
fill_form(common_driver)
sleep(10)
common_driver.quit()

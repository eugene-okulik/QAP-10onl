from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def open_browser():
    options = Options()
    options.add_argument('window-size=400,1000')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def student_registration_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Valeria')
    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Kondrateva')
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('test@gmail.com')
    gender = driver.find_element(By.XPATH, '//label[@for="gender-radio-2"]')
    gender.click()
    mobile = driver.find_element(By.ID, 'userNumber')
    mobile.send_keys('1234567')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()
    month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    my_month = Select(month)
    my_month.select_by_value('10')
    year = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    my_year = Select(year)
    my_year.select_by_value('1996')
    day = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--009')
    day.click()
    subject = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subject.click()
    subject.send_keys('Maths')
    subject.send_keys(Keys.ENTER)
    hobbies = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    hobbies.click()
    address = driver.find_element(By.ID, 'currentAddress')
    address.send_keys('Minskaya 10')
    state = driver.find_element(By.ID, 'state')
    state.click()
    my_state = driver.find_element(By.ID, 'react-select-3-input')
    my_state.send_keys('NCR')
    my_state.send_keys(Keys.ENTER)
    city = driver.find_element(By.ID, 'city')
    city.click()
    my_city = driver.find_element(By.ID, 'react-select-4-input')
    my_city.send_keys('Delhi')
    my_city.send_keys(Keys.ENTER)
    submit = driver.find_element(By.ID, 'submit')
    submit.submit()


common_driver = open_browser()
student_registration_form(common_driver)
common_driver.quit()

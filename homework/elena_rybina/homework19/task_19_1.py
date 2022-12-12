from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def open_browser():
    options = Options()
    options.add_argument('window-size=700,1500')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(20)
    return chrome_driver


def submit_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Elena')
    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Rybina')
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('karkar@gmail.com')
    gender = driver.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[2]/label')
    gender.click()
    mobile = driver.find_element(By.ID, 'userNumber')
    mobile.send_keys('4444444')
    DOB = driver.find_element(By.ID, 'dateOfBirthInput')
    DOB.click()
    birth_month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    birth_month_sel = Select(birth_month)
    birth_month_sel.select_by_index(6)
    birth_year = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    birth_year_sel = Select(birth_year)
    birth_year_sel.select_by_visible_text('1989')
    birth_day = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--007')
    birth_day.click()
    subjects = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subjects.click()
    subjects.send_keys('Bio')
    subjects.send_keys(Keys.ENTER)
    hobbies = driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')
    hobbies.click()
    address = driver.find_element(By.ID, 'currentAddress')
    address.send_keys('Sakhalin')
    state_window = driver.find_element(By.ID, 'state')
    state = state_window.find_element(By.XPATH, '//input[@id="react-select-3-input"]')
    state.send_keys('Har')
    state.send_keys(Keys.ENTER)
    city_window = driver.find_element(By.ID, 'city')
    city = city_window.find_element(By.XPATH, '//input[@id="react-select-4-input"]')
    city.send_keys('Kar')
    city.send_keys(Keys.ENTER)
    submit = driver.find_element(By.ID, 'submit')
    submit.submit()


driver = open_browser()
submit_form(driver)
sleep(7)
driver.quit()

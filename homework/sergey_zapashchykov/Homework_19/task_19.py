from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    # options.add_argument('window-size=1000,1000')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.implicitly_wait(10)
    return chrome_driver


def fill_out_the_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.click()
    first_name.send_keys('Sergey')
    first_name.send_keys(Keys.END)

    last_name = driver.find_element(By.ID, 'lastName')
    last_name.click()
    last_name.send_keys('Zapashchykov')
    last_name.send_keys(Keys.END)

    e_mail = driver.find_element(By.ID, 'userEmail')
    e_mail.click()
    e_mail.send_keys('po4ta@po4ta.com')
    e_mail.send_keys(Keys.END)

    gender_checkbox = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
    gender_checkbox.click()

    mobile_number = driver.find_element(By.ID, 'userNumber')
    mobile_number.click()
    mobile_number.send_keys('0123456789')
    mobile_number.send_keys(Keys.END)

    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.click()

    month = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__month-select')
    month.click()
    month_select = driver.find_element(By.XPATH, '//option[@value="2"]')
    month_select.click()
    year = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select')
    year.click()
    year_select = driver.find_element(By.XPATH, '//option[@value="1985"]')
    year_select.click()
    date = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--021')
    date.click()

    subjects = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subjects.click()
    subjects.send_keys('Computer Science')
    subjects.send_keys(Keys.ENTER)

    hobby_reading = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-2"]')
    hobby_reading.click()
    hobby_music = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    hobby_music.click()

    select_picture = driver.find_element(By.ID, 'uploadPicture')
    select_picture.send_keys('QAP-10onl/homework/sergey_zapashchykov/Homework_19/img/Computer-Science.png')

    address = driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]')
    address.click()
    address.send_keys('Vitebsk')
    address.send_keys(Keys.END)

    state = driver.find_element(By.ID, 'react-select-3-input')
    state.send_keys('Haryana')
    state.send_keys(Keys.ENTER)

    city = driver.find_element(By.ID, 'react-select-4-input')
    city.send_keys('Panipat')
    city.send_keys(Keys.ENTER)

    submit_button = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit_button.submit()

    modal_content = driver.find_element(By.CSS_SELECTOR, '.modal-content')
    print(modal_content.text)


common_driver = open_browser()
fill_out_the_form(common_driver)
sleep(5)
common_driver.quit()

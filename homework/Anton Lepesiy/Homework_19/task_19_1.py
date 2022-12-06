from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def open_browser():
    options = Options()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


def find_and_fill(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name_field = driver.find_element(By.ID, 'firstName')
    first_name_field.send_keys('Antoshka')
    last_name_field = driver.find_element(By.ID, 'lastName')
    last_name_field.send_keys('Kartoshka')
    mail_field = driver.find_element(By.ID, 'userEmail')
    mail_field.send_keys('antoshka.kartoshka@gmail.com')
    gender_choice = driver.find_element(By.XPATH, '//label[@class="custom-control-label"]')
    gender_choice.click()
    phone_field = driver.find_element(By.XPATH, '//input[@placeholder="Mobile Number"]')
    phone_field.send_keys('1234567890')
    birth_date = driver.find_element(By.ID, 'dateOfBirthInput')
    birth_date.click()
    year = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
    dropdown_year = Select(year)
    dropdown_year.select_by_value('2049')
    month = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    dropdown_month = Select(month)
    dropdown_month.select_by_visible_text('June')
    day = driver.find_element(By.CSS_SELECTOR, '.react-datepicker__day.react-datepicker__day--015')
    day.click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    subject = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    subject.click()
    subject.send_keys('biology')
    subject.send_keys(Keys.ENTER)
    hobby = driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-2"]')
    hobby.click()
    address = driver.find_element(By.XPATH, '//textarea[@placeholder="Current Address"]')
    address.send_keys('Night-city, ul. Przyszłośći 20/49')
    driver.execute_script("document.body.style.zoom = '0.5'")
    state = driver.find_element(By.ID, 'react-select-3-input')
    state.send_keys('NCR')
    state.send_keys(Keys.ENTER)
    city = driver.find_element(By.ID, 'react-select-4-input')
    city.send_keys('Gurgaon')
    city.send_keys(Keys.ENTER)
    submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
    submit.submit()


common_driver = open_browser()
find_and_fill(common_driver)
common_driver.quit()

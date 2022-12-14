from selenium.webdriver.common.by import By


password_field = (By.XPATH, '//input[@type="password"]')
confirm_password_field = (By.ID, 'password-confirmation')
create_an_account_button = (By.XPATH, '//button[@title="Create an Account"]')
error_massage = (By.CSS_SELECTOR, '#password-confirmation-error')

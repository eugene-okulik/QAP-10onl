from selenium.webdriver.common.by import By


first_name_field = (By.XPATH, '//input[@id="firstname"]')
password_field = (By.XPATH, '//input[@title="Password"]')
confirm_password_field = (By.XPATH, '//button[@type="submit"]')
create_account_button = (By.CSS_SELECTOR, '.submit')
error_massage = (By.XPATH, '//div[@for="password-confirmation"]')
first_name_field_full = (By.XPATH, '//input[@class="input-text required-entry valid"]')
password_strength_message = (By.ID, 'password-strength-meter-label')
checkbox_news = (By.ID, 'is_subscribed')

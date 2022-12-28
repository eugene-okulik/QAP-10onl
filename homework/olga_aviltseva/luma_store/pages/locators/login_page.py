from selenium.webdriver.common.by import By


email_field = (By.ID, 'email')
pass_field = (By.ID, 'pass')
send_button = (By.ID, 'send2')
validation_err = (By.XPATH, '//div[@for="email"]')
error_alert = (By.XPATH, '//div[@role="alert"]')

from selenium.webdriver.common.by import By


title_text = (By.CLASS_NAME, 'base')
create_account_button = (By.XPATH, '//span[normalize-space(text())="Create an Account"]')
required_fields = (By.CSS_SELECTOR, 'div[class="mage-error"]')

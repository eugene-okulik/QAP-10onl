from selenium.webdriver.common.by import By


title_text = (By.CLASS_NAME, 'base')
subscribe = (By.XPATH, '//span[normalize-space(text())="Subscribe"]')
content_blocks = (By.XPATH, '//strong[@class="title"]')

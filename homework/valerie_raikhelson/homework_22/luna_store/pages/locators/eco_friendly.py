from selenium.webdriver.common.by import By

products_list = (By.CSS_SELECTOR, '.product-items>li')
empty_items_to_compare = (By.CSS_SELECTOR, '.block-compare>.empty')
subscribe_btn = (By.CSS_SELECTOR, '.subscribe.primary')
email_err = (By.CSS_SELECTOR, '#newsletter-error')
select_amount_items = (By.CSS_SELECTOR, '.main>:nth-child(5) #limiter')

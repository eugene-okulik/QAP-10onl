from selenium.webdriver.common.by import By


products_list = (By.CLASS_NAME, "product-image-photo")
style_1_filter = (By.XPATH, '//div[@id="narrow-by-list"]//div[@class="filter-options-item"][1]//div[1]')
style_1_filter_content = (By.XPATH, '//div[@class="filter-options-item allow active"]')
base_layer_link = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/collections/eco-friendly.html'
                             '?style_bottom=104"]')

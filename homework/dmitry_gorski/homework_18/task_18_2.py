from common.utils import WebPage

web, driver = WebPage, WebPage.DRIVER
driver.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
elem_check_all = web.find_by_id('check1')
elem_check_all.click()
print(elem_check_all.get_attribute('value'))

elem_single_checkbox = web.find_by_class('cb1-element')
elem_single_checkbox.click()
print(elem_check_all.get_attribute('value'))
driver.quit()

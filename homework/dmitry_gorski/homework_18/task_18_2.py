from common.utils import WebPage

page = WebPage()
page.DRIVER.get('https://demo.seleniumeasy.com/basic-checkbox-demo.html')
elem_check_all = page.find_by_id('check1')
elem_check_all.click()
print(elem_check_all.get_attribute('value'))

elem_single_checkbox = page.find_by_class('cb1-element')
elem_single_checkbox.click()
print(elem_check_all.get_attribute('value'))
page.DRIVER.quit()

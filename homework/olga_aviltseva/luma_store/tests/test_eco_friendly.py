from pages.eco_friendly_page import EcoFriendlyPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure


@allure.feature('Eco Friendly')
@allure.story('Products list')
def test_products_count(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()

    assert eco_friendly.count_products_on_the_page() == 12


@allure.feature('Eco Friendly')
@allure.story('Left navigation panel')
def test_style_1_filter_content(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()
    WebDriverWait(driver, 10).until(ec.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'Default welcome msg!'))
    eco_friendly.click_style_1_filter()
    assert eco_friendly.check_style_1_content()


@allure.feature('Eco Friendly')
@allure.story('Left navigation panel')
def test_base_layer_link(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()
    eco_friendly.click_style_1_filter()
    eco_friendly.click_base_layer_link()
    assert eco_friendly.count_products_on_the_page() == 1

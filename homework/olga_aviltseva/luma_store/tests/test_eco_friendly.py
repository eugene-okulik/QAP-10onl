from pages.eco_friendly_page import EcoFriendlyPage
from time import sleep
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
    sleep(1)  # Не заменен  на WebDriverWait так как на странице ничего не меняется, из за быстрых кликов автотеста
    # не успевает срабатывать, поэтому стоит слип
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

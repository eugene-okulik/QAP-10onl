from pages.eco_friendly_page import EcoFriendlyPage
from time import sleep


def test_products_count(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()
    assert eco_friendly.count_products_on_the_page() == 12


def test_style_1_filter_content(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()
    sleep(3)  # Оставила специально, не забыла убрать
    eco_friendly.click_style_1_filter()
    assert eco_friendly.check_style_1_content()


def test_base_layer_link(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()
    eco_friendly.click_style_1_filter()
    eco_friendly.click_base_layer_link()
    assert eco_friendly.count_products_on_the_page() == 1

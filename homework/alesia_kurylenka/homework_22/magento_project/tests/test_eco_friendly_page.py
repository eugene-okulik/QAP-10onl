from pages.eco_friendly_page import EcoFriendlyPage


def test_eco_friendly_link(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.page_url == 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'


def test_products_count(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.products_count() == 12


def test_wish_lists_count(driver):
    eco_friendly_page = EcoFriendlyPage(driver)
    eco_friendly_page.open()
    assert eco_friendly_page.wish_lists_count() == 12

from pages.eco_friendly_page import EcoFriendlyPage


def test_eco_friendly_title(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()
    assert eco_friendly.check_title() == 'Eco Friendly'


def test_check_url(driver):
    eco_friendly = EcoFriendlyPage(driver)
    assert eco_friendly.check_url() == 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'


def test_check_products_on_the_page(driver):
    eco_friendly = EcoFriendlyPage(driver)
    assert eco_friendly.check_price_first_product() == '$40.00'

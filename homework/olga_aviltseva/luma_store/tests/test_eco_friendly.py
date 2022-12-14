from pages.eco_friendly_page import EcoFriendlyPage


def test_products_count(driver):
    eco_friendly = EcoFriendlyPage(driver)
    eco_friendly.open()
    assert eco_friendly.check_12_products_on_the_page() == 12

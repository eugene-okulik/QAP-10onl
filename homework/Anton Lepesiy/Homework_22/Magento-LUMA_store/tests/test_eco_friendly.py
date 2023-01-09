from pages.eco_friendly_page import EcoFriendly


def test_is_page_opened(driver):
    eco_friendly = EcoFriendly(driver)
    eco_friendly.open()
    assert eco_friendly.page_title()


def test_cart_showed(driver):
    eco_friendly = EcoFriendly(driver)
    eco_friendly.open()
    assert eco_friendly.cart().is_displayed()


def test_items_count(driver):
    eco_friendly = EcoFriendly(driver)
    eco_friendly.open()
    assert eco_friendly.displayed_items()

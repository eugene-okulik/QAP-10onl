from pages.eco_friendly import EcoFriendly


def test_is_page_opened(driver):
    eco_friendly = EcoFriendly(driver)
    eco_friendly.open()
    assert eco_friendly.is_page_opened()


def test_is_search_placeholder_shown(driver):
    eco_friendly = EcoFriendly(driver)
    eco_friendly.open()
    assert eco_friendly.is_search_placeholder_shown()


def test_is_search_suggest_shown(driver):
    eco_friendly = EcoFriendly(driver)
    eco_friendly.open()
    assert eco_friendly.is_search_suggest_shown()

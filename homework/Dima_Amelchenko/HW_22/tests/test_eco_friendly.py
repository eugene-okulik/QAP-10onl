from pages.eco_friendly_page import EcoFriendly
import allure


@allure.feature('Eco friendly')
@allure.story('Check title')
def test_eco_friendly_title(driver):
    eco_friendly = EcoFriendly(driver)
    eco_friendly.open()
    assert eco_friendly.check_title() == 'Eco Friendly'

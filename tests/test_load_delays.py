import pytest
import allure

from tests.pages import HomePage, LoadDelaysPage


@allure.feature("UI Test Automation")
@pytest.mark.load_delays
class TestLoadDelays:

    @allure.description("Verify that page loaded after long delay")
    def test_load_delays(self, home_page: HomePage):
        load_delays_page = home_page.navigate_to_page(LoadDelaysPage)
        load_delays_page.verify_button_is_visible()

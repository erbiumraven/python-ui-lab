import pytest
import allure

from tests.pages import ClientSideDelayPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.client_side_delay
class TestClientSideDelay:

    @allure.description("Verify label is visible after client side delay")
    def test_label_visible_after_client_side_delay(self, home_page: HomePage):
        client_side_delay_page = home_page.navigate_to_page(ClientSideDelayPage)
        client_side_delay_page.click_cta_button()
        client_side_delay_page.check_label_visible()

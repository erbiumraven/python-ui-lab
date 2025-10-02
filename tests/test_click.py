import pytest
import allure

from tests.pages import ClickPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.click
class TestClick:

    @allure.description("Verify that the button responds to a physical mouse click and changes state.")
    def test_physical_click_on_button(self, home_page: HomePage):
        click_page = home_page.navigate_to_page(ClickPage)
        click_page.click_button_with_mouse()
        click_page.assert_button_state_changed_after_mouse_click()

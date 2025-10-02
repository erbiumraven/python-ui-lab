import allure
import pytest

from tests.pages import HomePage, MouseOverPage


@allure.feature("UI Test Automation")
@pytest.mark.mouse_over
class TestMouseOver:

    @allure.description("Verify that hovering over links increments their click counts correctly")
    def test_hover_and_click_increments_counts(self, home_page: HomePage):
        mouse_over_page = home_page.navigate_to_page(MouseOverPage)

        mouse_over_page.hover_and_click_link()
        mouse_over_page.verify_click_count(
            mouse_over_page.get_click_count(),
            expected_count=1,
            element_name="Click me link"
        )

        mouse_over_page.hover_and_click_button_link()
        mouse_over_page.verify_click_count(
            mouse_over_page.get_button_click_count(),
            expected_count=1,
            element_name="Link Button"
        )

import allure
import pytest

from tests.pages import DisabledInputPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.disabled_input
class TestDisabledInputPage:

    @allure.description("Verify that a disabled input field can be enabled, text can be entered, "
                        "and the entered text is correctly displayed")
    def test_disabled_input_page(self, home_page: HomePage):
        disabled_input_page = home_page.navigate_to_page(DisabledInputPage)
        disabled_input_page.click_on_enable_button()
        text = 'jordan'
        disabled_input_page.enter_text_after_field_to_be_enabled(text)
        disabled_input_page.verify_text_entered(text)

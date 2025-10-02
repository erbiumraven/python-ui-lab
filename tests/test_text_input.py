import allure
import pytest

from tests.pages import HomePage, TextInputPage


@allure.feature("UI Test Automation")
@pytest.mark.text_input
class TestTextInput:

    @allure.description("Verify that typing text via the physical keyboard updates the button label correctly.")
    def test_button_label_updates_when_typing_via_keyboard(self, home_page: HomePage):
        text_to_type = "colorado"
        text_input_page = home_page.navigate_to_page(TextInputPage)
        text_input_page.input_text_by_physical_keyboard(text_to_type)
        text_input_page.click_on_button_with_changeable_label_text()
        text_input_page.assert_button_text_changed(text_to_type)

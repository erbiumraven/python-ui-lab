import pytest
import allure

from tests.pages import HiddenLayersPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.hidden_layers
class TestHiddenLayers:

    @allure.description("Verify that an hidden element is not interactable")
    def test_hidden_element_is_not_interactable(self, home_page: HomePage):
        hidden_layers_page = home_page.navigate_to_page(HiddenLayersPage)
        hidden_layers_page.click_green_button()

        hidden_layers_page.check_blue_button_is_visible()

        with allure.step("Click green button and verify that it is blocked by overlay"):
            with pytest.raises(Exception) as e:
                hidden_layers_page.click_green_button()

            expected_message = "subtree intercepts pointer events"
            assert expected_message in str(e.value), f"Expected message '{expected_message}' not found in exception"

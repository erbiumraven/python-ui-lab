import allure
import pytest

from tests.pages import NonBreakingSpacePage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.non_breaking_space
class TestNonBreakingSpace:

    @allure.description("Verify that the 'My Button' with non-breaking space is visible and interactable")
    def test_button_with_non_breaking_space_is_ready(self, home_page: HomePage):
        non_breaking_space_page = home_page.navigate_to_page(NonBreakingSpacePage)
        non_breaking_space_page.verify_button_is_interactable()

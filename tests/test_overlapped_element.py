import allure
import pytest

from tests.pages import HomePage, OverlappedElementPage


@allure.feature("UI Test Automation")
@pytest.mark.overlapped_element
class TestOverlappedElement:

    @allure.description("Verify overlapped element")
    def test_overlapped_element_using_default_approach(self, home_page: HomePage):
        overlapped_element_page = home_page.navigate_to_page(OverlappedElementPage)
        overlapped_element_page.fill_in_id_text_box("id")
        overlapped_element_page.fill_in_name_text_box("name")


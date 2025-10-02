import pytest
import allure

from helpers import assert_ids_are_different
from tests.pages import DynamicIdPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.dynamic_id
class TestDynamicId:

    @allure.description("Verify that the button can be clicked regardless of its dynamic ID")
    def test_button_click_without_using_dynamic_id(self, home_page: HomePage):
        dynamic_id_page = home_page.navigate_to_page(DynamicIdPage)
        dynamic_id_page.check_button_with_dynamic_id_clickable()
        first_id = dynamic_id_page.get_button_dynamic_id()

        dynamic_id_page.refresh()

        dynamic_id_page.check_button_with_dynamic_id_clickable()
        second_id = dynamic_id_page.get_button_dynamic_id()

        assert_ids_are_different(first_id, second_id)

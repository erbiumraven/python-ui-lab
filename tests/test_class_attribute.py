import pytest
import allure

from tests.pages import ClassAttributePage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.class_attribute
class TestClassAttribute:

    @allure.description("Verify that an element can be located by a specific class even if it has multiple classes.")
    def test_element_located_by_one_of_classes(self, home_page: HomePage):
        class_attribute_page = home_page.navigate_to_page(ClassAttributePage)
        class_attribute_page.click_primary_btn_and_check_alert_popup("Primary button pressed")

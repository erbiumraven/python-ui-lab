import pytest
import allure

from tests.pages import AjaxDataPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.ajax_data
class TestAjaxData:

    @allure.description("Verify label text is loaded by ajax request")
    def test_ajax_loaded_label_visible(self, home_page: HomePage):
        ajax_data_page = home_page.navigate_to_page(AjaxDataPage)
        ajax_data_page.click_ajax_loaded_button()
        ajax_data_page.check_ajax_loaded_label_visible()

import allure
import pytest

from tests.pages import HomePage, ShadowDomPage


@allure.feature("UI Test Automation")
@pytest.mark.shadow_dom
class TestShadowDom:

    @allure.description("Verify that a new ID can be generated in the Shadow DOM, copied to the clipboard,"
                        " and is not empty in the edit field.")
    def test_shadow_dom(self, home_page: HomePage):
        shadow_dom_page = home_page.navigate_to_page(ShadowDomPage)
        shadow_dom_page.generate_new_id()
        shadow_dom_page.copy_generated_id_to_clipboard()
        edit_field_value = shadow_dom_page.get_edit_field_value()
        assert edit_field_value != ""

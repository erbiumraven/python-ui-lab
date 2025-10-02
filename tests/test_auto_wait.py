import allure
import pytest

from tests.pages import AutoWaitPage, HomePage

from collections import namedtuple

ElementCondition = namedtuple("ElementCondition", ["condition", "element_type"])

ui_conditions = [
    ElementCondition("Visible", "Button"),
    ElementCondition("Visible", "Input"),
    ElementCondition("Enabled", "Textarea"),
    ElementCondition("Enabled", "Label"),
    ElementCondition("Editable", "Input"),
    ElementCondition("Editable", "Select"),
    ElementCondition("On Top", "Button"),
    ElementCondition("On Top", "Label"),
    ElementCondition("Non Zero Size", "Textarea"),
    ElementCondition("Non Zero Size", "Select"),
]


@allure.feature("UI Test Automation")
@pytest.mark.auto_wait
class TestAutoWait:

    @pytest.mark.parametrize("scenario", ui_conditions)
    def test_auto_wait(self, home_page: HomePage, scenario: ElementCondition):
        auto_wait_page = home_page.navigate_to_page(AutoWaitPage)
        auto_wait_page.select_element_by_type(scenario.element_type)
        auto_wait_page.set_condition(scenario.condition, check=False)
        auto_wait_page.apply_setting()
        auto_wait_page.verify_element_is_interactable(scenario.element_type)

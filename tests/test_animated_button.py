import allure
import pytest

from tests.pages import AnimatedButtonPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.animated_button
class TestAnimatedButton:

    @allure.description("")
    def test_animated_button(self, home_page: HomePage):
        animated_button_page = home_page.navigate_to_page(AnimatedButtonPage)
        animated_button_page.click_moving_target_when_stable()

import allure
import pytest

from tests.pages import HomePage, SampleAppPage


@allure.feature("UI Test Automation")
@pytest.mark.sample_app
class TestSampleApp:

    @allure.description("Verify that a user can log in and see the correct welcome message")
    def test_login_displays_welcome_message(self, home_page: HomePage):
        sample_app_page = home_page.navigate_to_page(SampleAppPage)

        username = "Carl"
        password = "pwd"

        sample_app_page.fill_in_username(username)
        sample_app_page.fill_in_password(password)
        sample_app_page.click_login()

        sample_app_page.verify_sample_app_welcome_message(username)

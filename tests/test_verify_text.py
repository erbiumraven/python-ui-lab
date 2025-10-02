import allure
import pytest

from playwright.sync_api import expect

from tests.pages import HomePage, VerifyTextPage


@allure.feature("UI Test Automation")
@pytest.mark.verify_text
class TestVerifyText:

    @allure.description("Verify that the welcome message on the Verify Text page contains the expected username")
    def test_verify_text(self, home_page: HomePage):
        verify_text_page = home_page.navigate_to_page(VerifyTextPage)
        expect(verify_text_page.welcome_locator).to_contain_text("Welcome UserName!")

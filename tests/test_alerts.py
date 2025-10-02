import allure
import pytest

from tests.pages import AlertsPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.alerts
class TestAlerts:

    @allure.description("Verify Alert, Confirm, and Prompt Dialogs")
    def test_alerts(self, home_page: HomePage):
        alerts_page = home_page.navigate_to_page(AlertsPage)
        alerts_page.verify_alert()
        alerts_page.verify_confirm()
        alerts_page.verify_prompt()

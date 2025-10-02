import allure

from playwright.sync_api import Page


class AlertsPage:
    PAGE_NAME = "Alerts"

    def __init__(self, page: Page):
        self.page = page
        self.alerts_heading = page.get_by_role("heading", name="Alerts")
        self.alert_button = page.get_by_role("button", name="Alert")
        self.confirm_button = page.get_by_role("button", name="Confirm")
        self.prompt_button = page.get_by_role("button", name="Prompt")

    def check_page_opened(self):
        self.alerts_heading.wait_for(state="visible", timeout=10000)

    def verify_alert(self):
        with allure.step("Click the alert button and verify the alert message"):
            def handle_dialog(dialog):
                assert "Today is a working day" in dialog.message
                dialog.accept()

            self.page.once("dialog", handle_dialog)

            self.alert_button.click()

    def verify_confirm(self):
        with allure.step("Click the confirm button and verify the confirm dialogs"):
            def handle_first_dialog(dialog):
                with allure.step("Verify first confirm dialog message contains 'Today is Friday.'"):
                    assert "Today is Friday." in dialog.message
                dialog.accept()

            def handle_second_dialog(dialog):
                with allure.step("Verify second confirm dialog message equals 'Yes'"):
                    assert dialog.message == "Yes"
                dialog.accept()

            self.page.once("dialog", handle_first_dialog)
            self.page.once("dialog", handle_second_dialog)
            self.confirm_button.click()

    def verify_prompt(self):
        with allure.step("Click the prompt button and handle prompt dialogs"):
            def handle_prompt_dialog(dialog):
                with allure.step("Verify prompt dialog message contains 'Enter your value' and enter 'dogs'"):
                    assert "Enter your value" in dialog.message
                    dialog.accept("dogs")

            def handle_result_dialog(dialog):
                with allure.step("Verify result dialog message equals 'dogs'"):
                    assert dialog.message == "dogs"
                dialog.accept()

            self.page.once("dialog", handle_prompt_dialog)
            self.page.once("dialog", handle_result_dialog)
            self.prompt_button.click()

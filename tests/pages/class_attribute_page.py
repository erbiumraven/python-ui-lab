import allure

from playwright.sync_api import Page, expect, Dialog


class ClassAttributePage:
    PAGE_NAME = "Class Attribute"

    def __init__(self, page: Page):
        self.page = page
        self.class_attribute_heading = self.page.get_by_role("heading", name="Class Attribute")
        self.scenario_heading = self.page.get_by_role("heading", name="Scenario")
        self.btn_primary = self.page.locator(
            "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")

    def check_page_opened(self):
        self.class_attribute_heading.wait_for(state="visible", timeout=10000)

    def click_primary_btn_and_check_alert_popup(self, expected_message: str):
        with allure.step(f"Verify alert popup with message: '{expected_message}'"):
            dialog_message = None

            def handle_dialog(dialog: Dialog):
                nonlocal dialog_message
                dialog_message = dialog.message
                dialog.accept()

            self.page.on("dialog", handle_dialog)
            self.btn_primary.click()
            self.page.wait_for_timeout(100)

            assert dialog_message == expected_message, f"Expected '{expected_message}', got '{dialog_message}'"

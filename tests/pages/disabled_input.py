import allure

from playwright.sync_api import Page, expect


class DisabledInputPage:
    PAGE_NAME = "Disabled Input"

    def __init__(self, page: Page):
        self.page = page
        self.disabled_input_heading = page.get_by_role("heading", name="Disabled Input")
        self.enabled_button = page.get_by_role("button", name="Enable Edit Field with 5")
        self.input_field = page.get_by_role("textbox", name="Edit Field")
        self.status_message = page.locator("#opstatus")

    def check_page_opened(self):
        with allure.step("Wait for the disabled input heading to be visible"):
            self.disabled_input_heading.wait_for(state="visible", timeout=10000)

    def click_on_enable_button(self):
        with allure.step("Click on the enable button"):
            self.enabled_button.click()

    def enter_text_after_field_to_be_enabled(self, text: str):
        with allure.step("Wait until the input field is enabled"):
            expect(self.input_field).to_be_enabled(timeout=10000)

        with allure.step(f"Enter text '{text}' into the input field and press Enter"):
            self.input_field.fill(text)
            self.input_field.press("Enter")

    def verify_text_entered(self, text: str):
        with allure.step(f"Verify that the status message shows 'Value changed to: {text}'"):
            expect(self.status_message).to_have_text(f"Value changed to: {text}")

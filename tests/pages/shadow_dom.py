import allure

from playwright.sync_api import Page


class ShadowDomPage:
    PAGE_NAME = "Shadow Dom"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.shadow_dom_heading = self.page.get_by_role("heading", name="Shadow DOM")
        self.edit_field = self.page.locator("#editField")
        self.copy_button = self.page.locator("guid-generator").locator("#buttonCopy")
        self.generate_button = self.page.locator("guid-generator").locator("#buttonGenerate")

    def check_page_opened(self):
        self.shadow_dom_heading.wait_for(state="visible", timeout=10000)

    def generate_new_id(self):
        with allure.step("Click the generate button to create a new ID"):
            self.generate_button.click()

    def copy_generated_id_to_clipboard(self):
        with allure.step("Click the copy button to copy the generated ID to the clipboard"):
            self.copy_button.click()

    def get_clipboard(self) -> str:
        with allure.step("Read the value from the clipboard"):
            return self.page.evaluate("navigator.clipboard.readText()")

    def get_edit_field_value(self) -> str:
        with allure.step("Get the value from the edit field"):
            return self.edit_field.input_value()

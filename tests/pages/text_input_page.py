import allure
from playwright.sync_api import Page


class TextInputPage:
    PAGE_NAME = "Text Input"

    def __init__(self, page: Page):
        self.page = page
        self.text_input_heading = self.page.get_by_role("heading", name="Text Input")
        self.text_input_field = self.page.get_by_role("textbox", name="Set New Button Name")
        self.button_with_changeable_label_text = self.page.locator("#updatingButton")

    def check_page_opened(self):
        self.text_input_heading.wait_for(state="visible", timeout=10000)

    def input_text_by_physical_keyboard(self, text: str):
        with allure.step("Input text by physical keyboard"):
            self.text_input_field.click()
            self.page.keyboard.type(text)

    def click_on_button_with_changeable_label_text(self):
        with allure.step("Click on button with changeable label text"):
            self.button_with_changeable_label_text.click()

    def assert_button_text_changed(self, expected_text: str):
        with allure.step(f"Assert button text changed to '{expected_text}'"):
            actual_text = self.button_with_changeable_label_text.inner_text()
            assert actual_text == expected_text, f"Expected button text to be '{expected_text}', but got '{actual_text}'"

import allure
from playwright.sync_api import Page, expect


class AutoWaitPage:
    PAGE_NAME = "Auto Wait"

    def __init__(self, page: Page):
        self.page = page
        self.auto_wait_heading = self.page.get_by_role("heading", name="Auto Wait")
        self.element_type_dropdown = self.page.get_by_label("Choose an element type:")
        self.apply_button = self.page.get_by_role("button", name="Apply 3s")

    def check_page_opened(self):
        self.auto_wait_heading.wait_for(state="visible", timeout=10000)

    def select_element_by_type(self, element_type: str):
        with allure.step(f"Select element type: {element_type}"):
            self.element_type_dropdown.select_option(element_type.lower())

    def set_condition(self, condition_name: str, check: bool = True):
        with allure.step(f"{'Check' if check else 'Uncheck'} condition: {condition_name}"):
            checkbox = self.page.get_by_role("checkbox", name=condition_name)
            if check:
                if not checkbox.is_checked():
                    checkbox.check()
            else:
                if checkbox.is_checked():
                    checkbox.uncheck()

    def apply_setting(self):
        with allure.step("Click 'Apply' button"):
            self.apply_button.click()

    def verify_element_is_interactable(self, element_type: str, input_text: str = "Test text"):
        with allure.step(f"Verify element is interactable: {element_type}"):
            if element_type == "Button":
                self.page.get_by_role("button", name="Button").click()
                expect(self.page.get_by_text("Target clicked.")).to_be_enabled()

            elif element_type == "Input":
                target = self.page.locator("#target")
                target.click()
                target.fill(input_text)
                target.press("Enter")
                expect(self.page.get_by_text("Text:")).to_be_enabled()

            elif element_type == "Textarea":
                target = self.page.locator("#target")
                target.click()
                target.fill(input_text)
                expect(self.page.get_by_text("Target clicked.")).to_be_enabled()

            elif element_type == "Select":
                target = self.page.locator("#target")
                target.select_option("Item 2")
                expect(self.page.get_by_text("Selected: Item")).to_be_enabled()

            elif element_type == "Label":
                self.page.get_by_text("This is a Label").click()
                expect(self.page.get_by_text("Target clicked.")).to_be_enabled()

            else:
                raise ValueError(f"Unknown element type: {element_type}")

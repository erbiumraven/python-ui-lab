import allure

from playwright.sync_api import Page, expect


class NonBreakingSpacePage:
    PAGE_NAME = "Non-Breaking Space"

    def __init__(self, page: Page):
        self.page = page
        self.non_breaking_space_page_heading = self.page.get_by_role("heading", name="Non-Breaking Space")
        self.button = self.page.locator("button", has_text="My Button")

    def check_page_opened(self):
        self.non_breaking_space_page_heading.wait_for(state="visible", timeout=10000)

    def verify_button_is_interactable(self):
        with allure.step("Verify that the button is enabled and interactable"):
            expect(self.button).to_be_enabled()

import allure

from playwright.sync_api import Page, expect


class LoadDelaysPage:
    PAGE_NAME = "Load Delay"

    def __init__(self, page: Page):
        self.page = page
        self.load_delays_heading = self.page.get_by_role("heading", name="Load Delays")
        self.scenario_heading = self.page.get_by_role("heading", name="Scenario")
        self.button = self.page.get_by_role("button", name="Button Appearing After Delay")

    def check_page_opened(self):
        self.load_delays_heading.wait_for(state="visible", timeout=10000)

    def verify_button_is_visible(self):
        with allure.step("Verify button is visible"):
            expect(self.button).to_be_visible(timeout=2000)

import allure

from playwright.sync_api import Page, expect


class HiddenLayersPage:
    PAGE_NAME = "Hidden Layers"

    def __init__(self, page: Page):
        self.page = page
        self.hidden_layers_heading = self.page.get_by_role("heading", name="Hidden Layers")
        self.scenario_heading = self.page.get_by_role("heading", name="Scenario")
        self.green_button = self.page.locator('#greenButton')
        self.blue_button = self.page.locator('#blueButton')

    def check_page_opened(self):
        self.hidden_layers_heading.wait_for(state="visible", timeout=10000)

    def click_green_button(self):
        with allure.step("Click green button"):
            self.green_button.click()

    def check_blue_button_is_visible(self):
        with allure.step("Check blue button is visible"):
            expect(self.blue_button).to_be_visible()

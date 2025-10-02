import allure

from playwright.sync_api import Page, expect


class DynamicIdPage:
    PAGE_NAME = "Dynamic ID"

    def __init__(self, page: Page):
        self.page = page
        self._init_locators()

    def _init_locators(self):
        self.dynamic_id_heading = self.page.get_by_role("heading", name="Dynamic ID")
        self.scenario_heading = self.page.get_by_role("heading", name="Scenario")
        self.button_with_dynamic_id = self.page.get_by_role("button", name="Button with Dynamic ID")
        self.home_link = self.page.get_by_role("link", name="Home")

    def check_page_opened(self):
        self.dynamic_id_heading.wait_for(state="visible", timeout=10000)

    def check_button_with_dynamic_id_clickable(self):
        with allure.step("Check that button with dynamic ID is visible, enabled, and click it"):
            expect(self.button_with_dynamic_id).to_be_visible()
            expect(self.button_with_dynamic_id).to_be_enabled()
            self.button_with_dynamic_id.click()

    def get_button_dynamic_id(self) -> str:
        with allure.step("Get the dynamic ID of the button"):
            return self.button_with_dynamic_id.get_attribute("id")

    def go_home(self):
        from tests.pages.home_page import HomePage
        self.home_link.click()
        home_page = HomePage(self.page)
        home_page.check_title_visible()
        return home_page

    def refresh(self):
        with allure.step("Refresh the Dynamic ID page"):
            self.page.reload()
            self._init_locators()
        return self

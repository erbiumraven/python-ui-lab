import allure

from playwright.sync_api import expect


class ClientSideDelayPage:
    PAGE_NAME = "Client Side Delay"

    def __init__(self, page):
        self.page = page
        self.clientside_delay_heading = self.page.get_by_role("heading", name="Client Side Delay")
        self.scenario_heading = self.page.get_by_role("heading", name="Scenario")
        self.cta_button = self.page.get_by_role("button", name="Button Triggering Client Side Logic")
        self.label = self.page.get_by_text("Data calculated on the client side.")

    def check_page_opened(self):
        self.clientside_delay_heading.wait_for(state="visible", timeout=10000)

    def click_cta_button(self):
        with allure.step("Click button to display data calculated on the client side"):
            self.cta_button.click()

    def check_label_visible(self):
        with allure.step("Check label is visible after clicking button"):
            expect(self.label).to_be_visible(timeout=20000)

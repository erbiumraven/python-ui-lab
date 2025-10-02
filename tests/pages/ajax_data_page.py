import allure

from playwright.sync_api import expect


class AjaxDataPage:
    PAGE_NAME = "Ajax Data"

    def __init__(self, page):
        self.page = page
        self.hidden_layers_heading = self.page.get_by_role("heading", name="AJAX Data")
        self.scenario_heading = self.page.get_by_role("heading", name="Scenario")
        self.cta_button = self.page.get_by_role("button", name="Button Triggering AJAX Request")
        self.ajax_loaded_label = self.page.get_by_text("Data loaded with AJAX get")

    def check_page_opened(self):
        self.hidden_layers_heading.wait_for(state="visible", timeout=10000)

    def click_ajax_loaded_button(self):
        with allure.step("Click button to load AJAX data"):
            self.cta_button.click()

    def check_ajax_loaded_label_visible(self):
        with allure.step("Check if AJAX data loaded with AJAX get"):
            expect(self.ajax_loaded_label).to_be_visible(timeout=20000)

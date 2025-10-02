import allure

from playwright.sync_api import expect

from tests.utils import click_element_center


class ClickPage:
    PAGE_NAME = "Click"

    def __init__(self, page):
        self.page = page
        self.click_heading = self.page.get_by_role("heading", name="Click")
        self.cta_button = self.page.get_by_role("button", name="Button That Ignores DOM Click")

    def check_page_opened(self):
        self.click_heading.wait_for(state="visible", timeout=10000)

    def click_button_with_mouse(self):
        with allure.step("Click Button with mouse (physical click)"):
            click_element_center(self.cta_button)

    def assert_button_state_changed_after_mouse_click(self):
        with allure.step("Verify that button state changed to success after mouse click"):
            expect(self.cta_button).to_have_class("btn btn-success")

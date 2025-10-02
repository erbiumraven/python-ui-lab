import allure

from playwright.sync_api import Page


class MouseOverPage:
    PAGE_NAME = "Mouse Over"

    def __init__(self, page: Page):
        self.page = page
        self.mouse_over_heading = self.page.get_by_role("heading", name="Mouse Over")
        self.click_count = self.page.locator("#clickCount")
        self.click_button_count = self.page.locator("#clickButtonCount")

    def check_page_opened(self):
        self.mouse_over_heading.wait_for(state="visible", timeout=10000)

    def get_click_me_link(self, title="Click me"):
        return self.page.locator(f"a[title='{title}']")

    def hover_and_click_link(self):
        with allure.step("Hover over 'Click me' link and click the new 'Active Link'"):
            self.get_click_me_link("Click me").hover()
            self.get_click_me_link("Active Link").click()

    def get_click_count(self):
        with allure.step("Get the current click count from '#clickCount'"):
            return int(self.click_count.inner_text())

    def hover_and_click_button_link(self):
        with allure.step("Hover over 'Link Button' and click it"):
            self.get_click_me_link("Link Button").hover()
            self.get_click_me_link("Link Button").click()

    def get_button_click_count(self):
        with allure.step("Get the current button click count from '#clickButtonCount'"):
            return int(self.click_button_count.inner_text())

    @allure.step("Verify click count of '{element_name}' is {expected_count}")
    def verify_click_count(self, actual_count: int, expected_count: int, element_name: str):
        assert actual_count == expected_count, (
            f"Expected click count of '{element_name}' to be {expected_count}, "
            f"but got {actual_count}"
        )
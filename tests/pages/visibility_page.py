import allure

from playwright.sync_api import Page


class VisibilityPage:
    PAGE_NAME = "Visibility"

    def __init__(self, page: Page):
        self.page = page
        self.visibility_heading = page.get_by_role("heading", name="Visibility")
        self.hide_button = self.page.hide_button = page.get_by_role("button", name="Hide")
        self.buttons_locators = {
            "removedButton": page.locator("#removedButton"),
            "zeroWidthButton": page.locator("#zeroWidthButton"),
            "overlappedButton": page.locator("#overlappedButton"),
            "transparentButton": page.locator("#transparentButton"),
            "invisibleButton": page.locator("#invisibleButton"),
            "notdisplayedButton": page.locator("#notdisplayedButton"),
            "offscreenButton": page.locator("#offscreenButton")
        }

    def check_page_opened(self):
        self.visibility_heading.wait_for(state="visible", timeout=10000)

    @allure.step("Click Hide button")
    def click_hide(self):
        self.hide_button.click()

    @allure.step("Check visibility of all buttons after Hide")
    def check_buttons_visibility(self):
        results = {}
        for name, locator in self.buttons_locators.items():
            is_visible = locator.is_visible()
            results[name] = is_visible
        return results

import allure
from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("h1#title", has_text="UI Test Automation")

    def get_page_link(self, page_name: str):
        return self.page.get_by_role("link", name=page_name)

    def check_title_visible(self):
        expect(self.title).to_be_visible()

    def goto(self, param, wait_until):
        self.page.goto(param, wait_until=wait_until)

    def navigate_to_page(self, page_class):
        page_name = page_class.PAGE_NAME
        with allure.step(f"Navigate to {page_name} page"):
            self.get_page_link(page_name).click()
            page_instance = page_class(self.page)
            page_instance.check_page_opened()
            return page_instance

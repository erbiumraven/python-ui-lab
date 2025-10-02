from playwright.sync_api import Page


class VerifyTextPage:
    PAGE_NAME = "Verify Text"

    def __init__(self, page: Page):
        self.page = page
        self.verify_text_heading = self.page.get_by_role("heading", name="Verify Text")
        self.welcome_locator = self.page.locator("//span[normalize-space(.)='Welcome UserName!']")

    def check_page_opened(self):
        self.verify_text_heading.wait_for(state="visible", timeout=10000)


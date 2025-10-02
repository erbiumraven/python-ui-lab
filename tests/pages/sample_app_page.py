import allure

from playwright.sync_api import Page, expect


class SampleAppPage:
    PAGE_NAME = "Sample App"

    def __init__(self, page: Page):
        self.page = page
        self.sample_app_heading = self.page.get_by_role("heading", name="Sample App")
        self.username = self.page.locator('input[name="UserName"]')
        self.password = self.page.locator('input[name="Password"]')
        self.log_in_btn = self.page.get_by_role("button", name="Log In")
        self.welcome_message = self.page.get_by_text("Welcome")

    def check_page_opened(self):
        self.sample_app_heading.wait_for(state="visible", timeout=10000)

    def fill_in_username(self, username: str):
        with allure.step(f"Fill in username: '{username}'"):
            self.username.fill(username)

    def fill_in_password(self, password: str):
        with allure.step(f"Fill in password: '{'*' * len(password)}'"):
            self.password.fill(password)

    def click_login(self):
        with allure.step("Click the Login button"):
            self.log_in_btn.click()

    def verify_sample_app_welcome_message(self, username: str):
        expected_message = f"Welcome, {username}!"
        with allure.step(f"Verify welcome message is '{expected_message}'"):
            expect(self.welcome_message).to_be_visible(timeout=5000)
            expect(self.welcome_message).to_have_text(expected_message, timeout=5000)

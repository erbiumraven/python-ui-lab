import allure

from playwright.sync_api import Page


class AnimatedButtonPage:
    PAGE_NAME = "Animated Button"

    def __init__(self, page: Page):
        self.page = page
        self.animated_button_heading = page.get_by_role("heading", name="Animated Button")
        self.moving_target_btn = page.locator("#movingTarget")
        self.start_animation_btn = page.locator("#animationButton")
        self.status_label = page.locator("#opstatus")

    def check_page_opened(self):
        self.animated_button_heading.wait_for(state="visible", timeout=10000)

    def click_moving_target_when_stable(self):
        with allure.step("Click the start animation button"):
            self.start_animation_btn.click()

        with allure.step("Wait until the moving target button stops spinning"):
            self.page.wait_for_function(
                """(el) => !el.classList.contains('spin')""",
                arg=self.moving_target_btn.evaluate_handle("el => el")
            )

        with allure.step("Click the moving target button once it is stable"):
            self.moving_target_btn.click()

        with allure.step("Verify the button no longer has the 'spin' class"):
            class_value = self.moving_target_btn.get_attribute("class")
            assert "spin" not in class_value, f"Button class still contains 'spin': {class_value}"

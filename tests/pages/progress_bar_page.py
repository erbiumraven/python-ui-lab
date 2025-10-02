import allure

import re
import time

from playwright.sync_api import Page


class ProgressBarPage:
    PAGE_NAME = "Progress Bar"

    def __init__(self, page: Page):
        self.page = page
        self.progressbar_heading = self.page.get_by_role("heading", name="Progress Bar")
        self.start_button = self.page.get_by_role("button", name="Start")
        self.stop_button = self.page.get_by_role("button", name="Stop")
        self.progress_indicator = self.page.get_by_role("progressbar")
        self.result_label = self.page.locator("#result")

    def check_page_opened(self):
        self.progressbar_heading.wait_for(state="visible", timeout=10000)

    def click_start_button(self):
        with allure.step("Click the start button to begin the progress"):
            self.start_button.click()

    def wait_progress_target_value_and_stop(self, target_value: int = 75):
        with allure.step(f"Wait until progress bar reaches {target_value} and then click stop"):
            while True:
                value_str = self.progress_indicator.get_attribute("aria-valuenow")
                if value_str is None:
                    raise RuntimeError("Progress bar attribute 'aria-valuenow' not found")

                value = int(value_str)

                if value >= target_value:
                    self.stop_button.click()
                    break

                time.sleep(0.2)

    def get_result_and_duration(self) -> tuple[int, int]:
        with allure.step("Retrieve result value and duration from the progress bar label"):
            text = self.result_label.inner_text()
            match = re.search(r"Result:\s*(\d+),\s*duration:\s*(\d+)", text)
            if not match:
                raise ValueError(f"Cannot parse result and duration from text: '{text}'")

            result_value = int(match.group(1))
            duration_value = int(match.group(2))
            return result_value, duration_value

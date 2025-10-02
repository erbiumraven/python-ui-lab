import allure
import pytest

from tests.pages import HomePage, ProgressBarPage
from helpers import assert_progressbar_result_with_tolerance


@allure.feature("UI Test Automation")
@pytest.mark.progressbar
class TestProgressBar:

    @allure.description("Verify that the progress bar reaches the target value within the allowed tolerance.")
    def test_progressbar(self, home_page: HomePage):
        progressbar_page = home_page.navigate_to_page(ProgressBarPage)
        progressbar_page.click_start_button()
        progressbar_page.wait_progress_target_value_and_stop()
        result, _ = progressbar_page.get_result_and_duration()
        assert_progressbar_result_with_tolerance(result, 0, 1)

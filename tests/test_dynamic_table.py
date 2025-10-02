import allure
import pytest

from tests.pages import DynamicTablePage, HomePage

from helpers import assert_cpu_values_match


@allure.feature("UI Test Automation")
@pytest.mark.dynamic_table
class TestDynamicTable:

    @allure.description(
        "This test verifies that the CPU value for Chrome displayed in the dynamic table "
        "matches the highlighted Chrome CPU warning text shown on the page."
    )
    def test_chrome_cpu_value_consistency(self, home_page: HomePage):
        dynamic_table_page = home_page.navigate_to_page(DynamicTablePage)
        cpu_cell_value = dynamic_table_page.get_cell_value_by_row_and_column(row_name="Chrome", column_name="CPU")
        cpu_warning_text = dynamic_table_page.chrome_cpu_locator.inner_text()

        assert_cpu_values_match(cpu_cell_value, cpu_warning_text)

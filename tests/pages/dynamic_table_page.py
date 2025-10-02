import allure

from playwright.sync_api import Page, expect


class DynamicTablePage:
    PAGE_NAME = "Dynamic Table"

    def __init__(self, page: Page):
        self.page = page
        self.table_locator = page.get_by_role("table")
        self.chrome_cpu_locator = page.get_by_text("Chrome CPU:", exact=False)

    def check_page_opened(self):
        self.table_locator.wait_for(state="visible", timeout=10000)

    import allure

    def get_cell_value_by_row_and_column(self, row_name: str, column_name: str) -> str:
        with allure.step(f"Locate the column index for '{column_name}'"):
            headers = self.table_locator.get_by_role("row").first.get_by_role("columnheader")
            column_index = None
            for i in range(headers.count()):
                if headers.nth(i).inner_text().strip() == column_name:
                    column_index = i
                    break
            if column_index is None:
                raise ValueError(f"Column '{column_name}' not found")

        with allure.step(f"Find the row containing '{row_name}'"):
            rows = self.table_locator.locator("div[role='rowgroup']").nth(1).get_by_role("row")
            matching_row = None
            for i in range(rows.count()):
                row = rows.nth(i)
                cell_texts = [
                    row.get_by_role("cell").nth(j).inner_text().strip()
                    for j in range(row.get_by_role("cell").count())
                ]
                if row_name in cell_texts:
                    matching_row = row
                    break
            if matching_row is None:
                raise ValueError(f"Row with '{row_name}' not found")

        with allure.step(f"Retrieve the cell value at row '{row_name}' and column '{column_name}'"):
            return matching_row.get_by_role("cell").nth(column_index).inner_text()

import allure


class ScrollbarPage:
    PAGE_NAME = "Scrollbars"

    def __init__(self, page):
        self.page = page
        self.scrollbars_heading = self.page.get_by_role("heading", name="Scrollbars")
        self.scrollable_container = self.page.locator("div[style*='overflow-y: scroll'][style*='overflow-x:scroll']")
        self.hiding_button = self.page.locator("#hidingButton")

    def check_page_opened(self):
        self.scrollbars_heading.wait_for(state="visible", timeout=10000)

    def scroll_to_button_using_bounding_box_coordinates(self):
        with allure.step("Scroll to button using bounding box"):
            box = self.hiding_button.bounding_box()
            if box:
                self.scrollable_container.evaluate(
                    "(container, coords) => { container.scrollLeft = coords.x; container.scrollTop = coords.y; }",
                    {"x": box["x"], "y": box["y"]}
                )

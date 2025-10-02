import allure

from playwright.sync_api import Page


class OverlappedElementPage:
    PAGE_NAME = "Overlapped Element"

    def __init__(self, page: Page):
        self.overlapped_element_heading = page.get_by_role("heading", name="Overlapped Element")
        self.id_textbox = page.get_by_role("textbox", name="Id")
        self.name_textbox = page.get_by_role("textbox", name="Name")

    def check_page_opened(self):
        self.overlapped_element_heading.wait_for(state="visible", timeout=10000)

    def fill_in_id_text_box(self, text: str):
        with allure.step(f"Fill in the ID text box with '{text}'"):
            self.id_textbox.fill(text)

    def fill_in_name_text_box(self, name: str):
        with allure.step(f"Fill in the Name text box with '{name}'"):
            self.name_textbox.fill(name)

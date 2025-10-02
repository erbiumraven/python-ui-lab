from playwright.sync_api import Page, expect


class FileUploadPage:
    PAGE_NAME = "File Upload"

    def __init__(self, page: Page):
        self.page = page
        self._init_locators()

    def _init_locators(self):
        self.file_upload_heading = self.page.get_by_role("heading", name="File Upload")
        self.upload_frame = self.page.frame_locator("iframe[src='/static/upload.html']")
        self.drop_area = self.upload_frame.locator("input[type='file']")
        self.file_input = self.upload_frame.locator("input[type='file']")
        self.selected_file_label = self.page.locator("iframe").content_frame.get_by_text("file(s) selected")

    def check_page_opened(self):
        self.file_upload_heading.wait_for(state="visible", timeout=10000)

    def upload_file_via_browse(self, file_path: str):
        self.file_input.set_input_files(file_path)
        expect(self.selected_file_label).to_be_visible(timeout=5000)

    def upload_file_via_drag_and_drop(self, file_path: str):
        self.drop_area.set_input_files(file_path)
        expect(self.selected_file_label).to_be_visible(timeout=5000)

    def refresh_page(self):
        self.page.reload()
        self._init_locators()

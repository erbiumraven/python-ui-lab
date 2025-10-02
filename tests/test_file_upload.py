import allure
import pytest

from tests.pages import FileUploadPage, HomePage


@allure.feature("UI Test Automation")
@pytest.mark.file_upload
class TestFileUpload:

    @allure.description(
        "Verify that a file can be uploaded via both the browse button and drag-and-drop functionality.")
    def test_file_upload(self, home_page: HomePage):
        file_upload_page = home_page.navigate_to_page(FileUploadPage)

        file_upload_page.upload_file_via_browse("tests/files/report.pdf")
        file_upload_page.refresh_page()
        file_upload_page.upload_file_via_drag_and_drop("tests/files/report.pdf")

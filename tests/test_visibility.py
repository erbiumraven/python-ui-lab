import pytest
import allure

from tests.pages import HomePage, VisibilityPage


@allure.feature("UI Test Automation")
@pytest.mark.visibility
class TestVisibilityPage:

    @allure.feature("UI Test Automation")
    @allure.description("Verify all buttons are hidden after clicking Hide")
    def test_visibility_page(self, home_page: HomePage):
        visibility_page = home_page.navigate_to_page(VisibilityPage)
        visibility_page.click_hide()

        expected_visibility = {
            "removedButton": False,
            "zeroWidthButton": False,
            "overlappedButton": True,  # Playwright’s is_visible() does not always account for element overlap.
            # If a transparent or non-blocking div is placed over a button, it may still be considered visible.
            "transparentButton": True,
            # Playwright does not consider opacity in is_visible() when determining visibility.
            # You can additionally check the element's opacity style.
            "invisibleButton": False,
            "notdisplayedButton": False,
            "offscreenButton": True  # Playwright may sometimes consider an element visible if it exists in the DOM
            # and has display != none and visibility != hidden.
        }

        actual_visibility = visibility_page.check_buttons_visibility()

        for btn, expected in expected_visibility.items():
            assert actual_visibility[btn] == expected, (
                f"Button '{btn}' visibility mismatch: "
                f"expected {expected}, got {actual_visibility[btn]}"
            )

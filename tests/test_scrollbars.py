import pytest
import allure

from tests.pages import HomePage, ScrollbarPage

from helpers import (
    assert_element_is_visible_in_scrollable_areas,
    assert_element_is_not_visible_in_scrollable_areas
)


@allure.feature("UI Test Automation")
@pytest.mark.scrollbars
class TestScrollbarsPage:

    @allure.description("Verify that the hiding button is initially hidden and becomes visible after"
                        " clicking it using the default approach.")
    def test_scroll_using_default_approach(self, home_page: HomePage):
        scrollbars_page = home_page.navigate_to_page(ScrollbarPage)
        assert_element_is_not_visible_in_scrollable_areas(
            scrollbars_page.hiding_button,
            scrollbars_page.scrollable_container
        )

        scrollbars_page.hiding_button.click()
        assert_element_is_visible_in_scrollable_areas(
            scrollbars_page.hiding_button,
            scrollbars_page.scrollable_container
        )

    @allure.description("Verify that the hiding button is initially hidden and becomes visible after "
                        "scrolling to it using bounding box coordinates.")
    def test_scroll_using_bounding_box_coordinates(self, home_page: HomePage):
        scrollbars_page = home_page.navigate_to_page(ScrollbarPage)
        assert_element_is_not_visible_in_scrollable_areas(
            scrollbars_page.hiding_button,
            scrollbars_page.scrollable_container
        )

        scrollbars_page.scroll_to_button_using_bounding_box_coordinates()
        scrollbars_page.hiding_button.click()
        assert_element_is_visible_in_scrollable_areas(
            scrollbars_page.hiding_button,
            scrollbars_page.scrollable_container
        )

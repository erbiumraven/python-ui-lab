import allure

from tests.utils import is_element_inside_container


def assert_ids_are_different(first_id: str, second_id: str):
    with allure.step("Verify that dynamic IDs are different"):
        allure.attach(first_id, name="First button ID", attachment_type=allure.attachment_type.TEXT)
        allure.attach(second_id, name="Second button ID", attachment_type=allure.attachment_type.TEXT)
        assert first_id != second_id, "The button IDs should be different!"


def assert_element_is_visible_in_scrollable_areas(element, container):
    with allure.step("Verify that element is visible in scrollable container"):
        assert is_element_inside_container(element, container), (
            "The element should be at least partially visible inside the scrollable container!"
        )


def assert_element_is_not_visible_in_scrollable_areas(element, container):
    with allure.step("Verify that element is NOT visible in scrollable container"):
        assert not is_element_inside_container(element, container), (
            "The element should NOT be visible inside the scrollable container!"
        )


def assert_cpu_values_match(cpu_cell_value: str, cpu_warning_text: str):
    with allure.step("Verify that Chrome CPU value from table matches the warning text"):
        assert cpu_cell_value in cpu_warning_text, (
            f"CPU value mismatch: expected '{cpu_cell_value}' to be part of '{cpu_warning_text}'"
        )


def assert_progressbar_result_with_tolerance(actual_result: int, expected_result: int, tolerance: int = 1):
    with allure.step(f"Verify result value with tolerance {tolerance}"):
        assert abs(actual_result - expected_result) <= tolerance, (
            f"Result value {actual_result} is outside the allowed tolerance ±{tolerance} "
            f"(expected {expected_result})"
        )

from playwright.sync_api import Locator


def click_element_center(element: Locator):
    box = element.bounding_box()
    if box is None:
        raise ValueError("Element is not visible or detached from DOM")

    x = box["x"] + box["width"] / 2
    y = box["y"] + box["height"] / 2
    element.page.mouse.click(x, y)

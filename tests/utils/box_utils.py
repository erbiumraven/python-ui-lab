def get_viewport_size(page):
    return page.viewport_size


def get_page_size(page):
    return page.evaluate("""
        () => ({
            width: document.documentElement.scrollWidth,
            height: document.documentElement.scrollHeight
        })
    """)


def get_element_size(locator):
    box = locator.bounding_box()
    return {"width": box["width"], "height": box["height"]} if box else None


def get_element_box_in_viewport(locator):
    return locator.evaluate("""
        el => {
            const rect = el.getBoundingClientRect();
            return { x: rect.x, y: rect.y, width: rect.width, height: rect.height }
        }
    """)


def is_element_inside_container(element_locator, container_locator, full_visibility=False):
    element_box = element_locator.evaluate("""
        el => {
            const rect = el.getBoundingClientRect();
            return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
        }
    """)

    container_box = container_locator.evaluate("""
        el => {
            const rect = el.getBoundingClientRect();
            return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
        }
    """)

    if full_visibility:
        horizontal = (
                element_box["x"] >= container_box["x"] and
                element_box["x"] + element_box["width"] <= container_box["x"] + container_box["width"]
        )
        vertical = (
                element_box["y"] >= container_box["y"] and
                element_box["y"] + element_box["height"] <= container_box["y"] + container_box["height"]
        )
    else:
        horizontal = (
                element_box["x"] + element_box["width"] > container_box["x"] and
                element_box["x"] < container_box["x"] + container_box["width"]
        )
        vertical = (
                element_box["y"] + element_box["height"] > container_box["y"] and
                element_box["y"] < container_box["y"] + container_box["height"]
        )

    return horizontal and vertical


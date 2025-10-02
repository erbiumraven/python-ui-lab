import os
from typing import Generator

import allure
import pytest
from playwright.sync_api import Page, sync_playwright

from tests.pages.home_page import HomePage

BASE_URL = os.getenv("BASE_URL", "http://www.uitestingplayground.com")


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-web-security",
                "--disable-features=IsolateOrigins,site-per-process",
                "--disable-blink-features=AutomationControlled",
                f"--unsafely-treat-insecure-origin-as-secure={BASE_URL}"
            ]
        )
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(
        base_url=BASE_URL,
        permissions=["clipboard-read", "clipboard-write"])
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def home_page(page: Page) -> Generator[HomePage, None, None]:
    with allure.step("Open Home page"):
        home = HomePage(page)
        home.goto("/", wait_until="load")
        home.check_title_visible()
    yield home


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")

import os

import pytest

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture
def user_credentials(request):
    return request.param

@pytest.fixture
def browser_instance(playwright,request):
    browser_name=request.config.getoption("--browser_name")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)
    elif browser_name == "edge":
        browser = playwright.chromium.launch(channel="msedge", headless=True)
        ### pytest playwrightdemo/test_framework_web_api.py --browser chromium --browser-channel msedge
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield page
    os.makedirs("test-results", exist_ok=True)
    context.tracing.stop(path=f"test-results/{request.node.name}.zip")
    context.close()
    browser.close()



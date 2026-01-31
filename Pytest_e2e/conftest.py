import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    #driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    yield driver  # Before Test function execution
    driver.close() #Post your test pytest Pytest_e2e/test_sortTable.pyfunction execution


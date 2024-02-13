import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_manage():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 975
    browser.config.window_height = 985

    yield

    browser.quit()
import pytest
from selene import browser

from utils import attach


@pytest.fixture(scope="function", autouse=True)
def browser_manage():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.window_width = 1420
    browser.config.window_height = 1080

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
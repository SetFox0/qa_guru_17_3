import pytest
from selene import browser


@pytest.fixture()
def setting_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 960
    browser.open('https://google.com/ncr')
    yield
    browser.quit()

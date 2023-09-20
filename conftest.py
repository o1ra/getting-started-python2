import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://google.com')
    yield
    browser.quit()

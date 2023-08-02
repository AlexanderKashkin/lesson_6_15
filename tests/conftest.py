import pytest

from config import browser


@pytest.fixture(scope='function', params=[(360, 800), (360, 640)], ids=['Model_1', 'Model_2'])
def window_size_mobile(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()


@pytest.fixture(scope='function', params=[(1366, 768), (1920, 1080)], ids=['WXGA', 'FullHD'])
def window_size_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()


@pytest.fixture(scope='function', params=[(1366, 768), (1920, 1080), (360, 800), (360, 640)],
                ids=['WXGA', 'FullHD', 'Model_1', 'Model_2'])
def window_size_all(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()

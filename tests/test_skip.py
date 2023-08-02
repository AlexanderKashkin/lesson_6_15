import pytest

from config import browser
from ..models_homework import github_desktop, github_mobile, is_mobile


def test_mobile_skip(window_size_all):
    if is_mobile(browser.config.window_width, browser.config.window_height):
        pytest.skip('bla-bla-bla')
    github_desktop(browser)


def test_desktop_skip(window_size_all):
    if not is_mobile(browser.config.window_width, browser.config.window_height):
        pytest.skip('bla-bla-bla')
    github_mobile(browser)

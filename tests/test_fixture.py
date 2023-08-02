from config import browser
from ..models_homework import github_desktop, github_mobile


def test_fixture_desktop(window_size_desktop):
    github_desktop(browser)


def test_fixture_mobile(window_size_mobile):
    github_mobile(browser)

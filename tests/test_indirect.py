import pytest

from config import browser
from models_homework import github_desktop, github_mobile


@pytest.mark.parametrize("window_size_desktop", [(2048, 1080)], ids=['2K'], indirect=True)
def test_indirect_desktop(window_size_desktop):
    github_desktop(browser)


@pytest.mark.parametrize("window_size_mobile", [(750, 1334)], ids=['iPhone 8'], indirect=True)
def test_indirect_mobile(window_size_mobile):
    github_mobile(browser)

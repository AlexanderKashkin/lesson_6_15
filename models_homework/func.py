from selene import have

from models_homework import GitHubElementsLoginPage


def github_mobile(browser) -> None:
    browser.open(GitHubElementsLoginPage.address)
    browser.element(GitHubElementsLoginPage.burger_mobile).click()
    browser.element(GitHubElementsLoginPage.login_mobile).click()
    browser.element(GitHubElementsLoginPage.assert_headers).should(have.exact_text(GitHubElementsLoginPage.assert_text))


def github_desktop(browser) -> None:
    browser.open(GitHubElementsLoginPage.address)
    browser.element(GitHubElementsLoginPage.login_desktop).click()
    browser.element(GitHubElementsLoginPage.assert_headers).should(have.exact_text(GitHubElementsLoginPage.assert_text))


def is_mobile(w: int, h: int) -> bool:
    return w < h

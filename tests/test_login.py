"""Login examples against https://www.saucedemo.com/."""

from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_standard_user_can_log_in(app_page: Page, test_users: dict) -> None:
    """A valid demo account should land on the inventory page."""
    login_page = LoginPage(app_page)
    user = test_users["standard_user"]

    login_page.load()
    login_page.login(user["username"], user["password"])

    expect(app_page).to_have_url("https://www.saucedemo.com/inventory.html")
    HomePage(app_page).expect_loaded()


def test_locked_out_user_sees_clear_error(app_page: Page, test_users: dict) -> None:
    """A locked account should show a useful error and remain on login."""
    login_page = LoginPage(app_page)
    user = test_users["locked_out_user"]

    login_page.load()
    login_page.login(user["username"], user["password"])

    login_page.expect_error("Sorry, this user has been locked out")

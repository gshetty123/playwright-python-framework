"""Home page checks against Sauce Demo's public inventory page."""

from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_inventory_home_page_shows_products(app_page: Page, test_users: dict) -> None:
    """After login, the inventory home page should show product content."""
    user = test_users["standard_user"]
    LoginPage(app_page).load()
    LoginPage(app_page).login(user["username"], user["password"])

    HomePage(app_page).expect_loaded()
    HomePage(app_page).expect_products_visible()

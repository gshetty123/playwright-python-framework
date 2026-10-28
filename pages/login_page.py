"""Page object for the Sauce Demo login form."""

from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from utils.config import SAUCE_DEMO_URL


class LoginPage(BasePage):
    # Locators live in the page object so tests focus on user behavior.
    username_input = "[data-test='username']"
    password_input = "[data-test='password']"
    login_button = "[data-test='login-button']"
    error_message = "[data-test='error']"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def load(self) -> None:
        self.open(SAUCE_DEMO_URL)

    def login(self, username: str, password: str) -> None:
        self.page.locator(self.username_input).fill(username)
        self.page.locator(self.password_input).fill(password)
        self.page.locator(self.login_button).click()

    def expect_error(self, message: str) -> None:
        expect(self.page.locator(self.error_message)).to_contain_text(message)

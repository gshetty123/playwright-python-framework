# Python + Playwright UI Test Framework

A small, beginner-friendly UI automation project using Python, synchronous Playwright, pytest, page objects, JSON test data, and self-contained HTML reports.

## Demo websites

- Login tests use [Sauce Demo](https://www.saucedemo.com/) and its published sample accounts. The standard and locked-out account behavior is part of the site's demo data, but public demo sites can change or be unavailable. Treat failures there as a possible site change and check the page manually.
These are public demo pages. The tests are examples, not checks for a service that this project controls. The site, sample accounts, selectors, or content may change, so check the live page when a test starts failing.

## Architecture

`tests/` holds readable test scenarios. `pages/` holds page objects: `BasePage` provides shared navigation, and each specific page class owns its locators and actions. `fixtures/browser_fixtures.py` provides a small `app_page` alias around the `page` fixture supplied by `pytest-playwright`, so browser lifecycle setup and teardown are already handled. `conftest.py` loads JSON test data. `test_data/users.json` keeps sample account data outside the test code. `utils/config.py` centralizes URLs and timeout settings. `reports/` receives the generated HTML report.

The page object pattern keeps tests focused on what a user does, while selectors and page-specific behavior stay together in their page class. Pytest fixtures provide each test a fresh page and load the JSON data when requested.

## Prerequisites and installation

Install Python 3.9 or newer and use a terminal opened at this project folder. On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install chromium
```

If PowerShell blocks activation, you can run commands using `.venv\Scripts\python.exe` directly instead of activating the environment. Chromium is the default browser for pytest-playwright; install other browsers with `python -m playwright install firefox` or `webkit` if needed.

## Run tests

Run all tests:

```powershell
pytest
```

Run one test file:

```powershell
pytest tests/test_login.py
```

Run one named test:

```powershell
pytest tests/test_login.py::test_standard_user_can_log_in
```

Pytest uses pytest-playwright's `page` fixture to open and close a browser page for each test. To see the browser while tests run, add `--headed`; to select a browser, add `--browser firefox` (after installing that browser).

## HTML reports

`pytest.ini` configures pytest-html to write `reports/report.html` as a self-contained report. Run `pytest`, then open that file in a browser. The generated report is ignored by Git so it does not clutter portfolio commits. To choose another report path, override the options, for example:

```powershell
pytest --html=reports/login-report.html --self-contained-html
```

## Add a page object and test

1. Create a class in `pages/`, accept a Playwright `Page`, and keep that page's locators and user actions in the class. Inherit from `BasePage` if the shared `open()` method is useful.
2. Add URLs or other reusable settings to `utils/config.py`. Put reusable data in `test_data/` when appropriate.
3. Create a `tests/test_*.py` file. Request `app_page` (or pytest-playwright's `page`) and any data fixtures in the test function, call page-object methods, and use Playwright's `expect(...)` assertions.
4. Run the new test with `pytest tests/test_your_feature.py` and inspect the report.

For example, a new test can construct `ProductsPage(app_page)`, call `open()` or a page-specific action, then assert a user-visible result. Prefer role, label, and test-id locators when a site provides them; confirm selectors against the current demo page when it changes.

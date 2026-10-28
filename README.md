# Python + Playwright UI Test Automation Framework

A beginner-friendly UI automation framework built with **Python, Playwright, and Pytest**, following the Page Object Model (POM). It demonstrates reusable fixtures, external JSON test data, and HTML test reporting.

## Features

- Python with Playwright's synchronous API
- Pytest-based test execution and reusable fixtures
- Page Object Model for maintainable test scripts
- External test data stored in JSON
- Centralized configuration for URLs and timeouts
- HTML test reports using `pytest-html`
- GitHub-ready project structure

## Demo Website

Login tests use [Sauce Demo](https://www.saucedemo.com/) and its published sample accounts.

The tests demonstrate successful login, locked-out user handling, and product-page verification. Sauce Demo is a public demonstration website, so its content, selectors, sample accounts, or availability may change. Failures should be investigated against the live website before being treated as framework defects.

## Project Architecture

```text
playwright-python-framework/
├── tests/
│   ├── test_login.py
│   └── test_home_page.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── home_page.py
├── fixtures/
│   └── browser_fixtures.py
├── test_data/
│   └── users.json
├── utils/
│   └── config.py
├── reports/
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Folder responsibilities

| Component | Purpose |
|---|---|
| `tests/` | Contains readable test scenarios and assertions. |
| `pages/` | Contains page objects, locators, and page-specific actions. |
| `pages/base_page.py` | Provides shared page functionality. |
| `fixtures/` and `conftest.py` | Support reusable test setup and fixtures. |
| `test_data/` | Stores sample user data in JSON format. |
| `utils/config.py` | Centralizes reusable configuration values. |
| `reports/` | Stores generated HTML reports. |
| `pytest.ini` | Configures Pytest and report options. |
| `requirements.txt` | Lists Python dependencies. |

The Page Object Model keeps test scenarios separate from page-specific locators and actions. This makes the framework easier to maintain and extend.

## Prerequisites

- Python 3.9 or newer
- Git
- Visual Studio Code or another Python editor

## Installation

Open a terminal in the project directory.

### 1. Create a virtual environment

```powershell
py -m venv .venv
```

### 2. Activate the environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use `.venv\Scripts\python.exe` to run Python commands directly.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install the Playwright browser

```powershell
python -m playwright install chromium
```

## Running Tests

Run the entire test suite:

```powershell
python -m pytest
```

Run the login tests:

```powershell
python -m pytest tests/test_login.py
```

Run a specific test:

```powershell
python -m pytest tests/test_login.py::test_standard_user_can_log_in
```

Run tests with the browser visible:

```powershell
python -m pytest --headed
```

## HTML Test Reports

The framework uses `pytest-html` to generate an HTML report.

Run the test suite:

```powershell
python -m pytest
```

Open the generated report:

```powershell
Invoke-Item .\reports\report.html
```

The report provides a convenient way to review test execution results. Generated reports are excluded from Git commits to keep the repository clean.

To generate a separate report for a specific run:

```powershell
python -m pytest tests/test_login.py --html=reports/login-report.html --self-contained-html
```

## Adding a New Test

1. Create a page class in `pages/` and define its locators and user actions.
2. Reuse `BasePage` functionality where appropriate.
3. Add reusable configuration to `utils/config.py` and test data to `test_data/` when needed.
4. Create a test file named `test_*.py` in `tests/`.
5. Use the available fixtures and Playwright assertions.
6. Run the test and inspect the HTML report.

## Project Status

The initial framework is implemented, and the current test suite has passed all three tests in the local development environment.

This is a portfolio and learning project intended to demonstrate UI automation framework design, test organization, and reporting. It is not affiliated with or maintained by Sauce Labs.

## Future Improvements

- Add more positive and negative test scenarios
- Expand reusable page objects and assertions
- Integrate API testing
- Add continuous integration with GitHub Actions


[![Playwright Tests](https://github.com/gshetty123/playwright-python-framework/actions/workflows/playwright-tests.yml/badge.svg?branch=master)](https://github.com/gshetty123/playwright-python-framework/actions/workflows/playwright-tests.yml)
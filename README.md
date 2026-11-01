# Python + Playwright UI Test Automation Framework

[![Playwright Tests](https://github.com/gshetty123/playwright-python-framework/actions/workflows/playwright-tests.yml/badge.svg?branch=master)](https://github.com/gshetty123/playwright-python-framework/actions/workflows/playwright-tests.yml)

A Python-based UI test automation framework built using **Playwright and Pytest**, following the **Page Object Model (POM)** design pattern.

This project demonstrates maintainable automation practices, reusable fixtures, data-driven testing using external JSON files, automated HTML reporting, failure screenshots, and continuous integration with GitHub Actions.

It demonstrates practical capabilities in functional testing, regression testing, and web UI automation.

## Key Features

- **Browser Automation:** Web UI automation using Playwright with Chromium.
- **Test Framework:** Pytest-based execution with reusable fixtures.
- **Page Object Model:** Organized page classes for maintainable automation.
- **Data-Driven Testing:** External JSON files for managing test credentials and test data.
- **Reusable Components:** Shared page functionality and centralized configuration.
- **Automated Reporting:** Self-contained HTML test reports using `pytest-html`.
- **Failure Screenshots:** Automatically captures screenshots when tests fail.
- **Continuous Integration:** GitHub Actions workflow for automated test execution.
- **Version Control:** Git-based source control and GitHub repository management.

## Project Architecture

```text
playwright-python-framework/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
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
│   └── screenshots/
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Folder Responsibilities

| Component | Responsibility |
|---|---|
| `tests/` | Contains test scenarios, execution logic, and assertions. |
| `pages/` | Implements Page Object Model classes, locators, and page-specific actions. |
| `pages/base_page.py` | Provides reusable methods shared across page classes. |
| `fixtures/` | Provides browser and page fixtures for test execution. |
| `conftest.py` | Manages shared Pytest fixtures and automatic failure screenshots. |
| `test_data/` | Stores external JSON test data and sample user credentials. |
| `utils/` | Contains reusable configuration and helper modules. |
| `.github/workflows/` | Configures automated test execution through GitHub Actions. |
| `reports/` | Stores generated HTML reports and failure screenshots locally. |
| `pytest.ini` | Defines Pytest discovery and reporting configuration. |
| `requirements.txt` | Lists the Python dependencies required by the framework. |

## Installation and Execution

### Prerequisites

- Python 3.10 or later
- Git
- pip

### Clone the repository

```bash
git clone https://github.com/gshetty123/playwright-python-framework.git

cd playwright-python-framework
```

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Install Playwright browser

```bash
python -m playwright install chromium
```

### Run the tests

```bash
python -m pytest
```

### Run tests in headed mode

```bash
python -m pytest --headed
```

## Adding a New Test

Follow these steps to add a new UI automation test:

1. Create or update the relevant Page Object class in the `pages/` directory.
2. Define reusable locators and page-specific actions in the Page Object class.
3. Add test data to `test_data/users.json` if required.
4. Create a new test file in the `tests/` directory using the `test_` naming convention.
5. Use the shared fixtures and Page Object methods in your test.
6. Add assertions to validate the expected application behaviour.
7. Run the test suite using `python -m pytest`.

This approach keeps test scenarios readable, reusable, and maintainable.

## Project Status

The framework is implemented and published on GitHub.

Current capabilities include:

- Three UI automation test scenarios covering login and product-page functionality.
- Reusable Page Object Model architecture.
- External JSON-based test data management.
- Automated HTML test reporting.
- Automatic screenshots on test failures.
- GitHub Actions integration for continuous test execution.

All three existing tests have passed in the local development environment, and the GitHub Actions workflow has completed successfully.

This project demonstrates practical skills in Python-based UI automation, functional testing, regression testing, test framework design, and continuous integration.

## QA Automation Services

I can help teams improve their web application testing through:

- **UI Automation:** Automating repetitive web application workflows using Python and Playwright.
- **Functional Testing:** Validating application features against business requirements.
- **Regression Testing:** Automating existing test scenarios to identify unexpected changes.
- **Test Framework Development:** Building reusable automation frameworks using Pytest and Page Object Model.
- **Failure Analysis:** Capturing screenshots and investigating failed test scenarios.
- **CI Integration:** Configuring automated test execution using GitHub Actions.

For freelance QA automation projects, I can help with test automation, framework setup, and regression test coverage.

## Future Improvements

- Expand UI automation coverage with additional positive and negative test scenarios.
- Introduce API testing using Playwright's API capabilities.
- Add cross-browser execution for Chromium, Firefox, and WebKit.
- Integrate advanced test reporting with Allure.
- Improve test execution through parallel testing.
- Explore Jenkins integration for CI/CD pipeline execution.

## Demo Application and Test Coverage

**Application:** [Sauce Demo](https://www.saucedemo.com/)

The framework currently automates the following scenarios:

| Test Scenario | Expected Result |
|---|---|
| Standard user login | User successfully logs in. |
| Locked-out user login | Appropriate error message is displayed. |
| Inventory page validation | Products are displayed after successful login. |

These scenarios demonstrate functional UI testing, positive and negative test coverage, and validation of application behaviour.

**Note:** Sauce Demo is a public demonstration application. Its availability and behaviour may change independently of this framework. This is an independent portfolio project and is not affiliated with Sauce Labs.

## Test Reporting and Failure Screenshots

The framework uses `pytest-html` to generate self-contained HTML test reports.

### Generate the HTML report

Run the complete test suite:

```powershell
python -m pytest
```

The report is generated at:

```text
reports/report.html
```

Open the report in your default browser:

```powershell
Invoke-Item .\reports\report.html
```

### Automatic Failure Screenshots

The framework captures screenshots automatically when a test fails during execution.

Screenshots are saved in:

```text
reports/screenshots/
```

Each screenshot uses the corresponding test name as its filename.

This helps investigate UI failures and provides visual evidence for debugging.

**Note:** Generated reports and screenshots are excluded from Git commits through `.gitignore`.

## Continuous Integration with GitHub Actions

The framework uses GitHub Actions to automate Playwright test execution.

The workflow is configured in:

`.github/workflows/playwright-tests.yml`

### Workflow triggers

- Push to the `master` branch.
- Pull requests targeting the `master` branch.
- Manual execution through GitHub Actions.

### Automated workflow steps

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs project dependencies.
4. Installs Playwright and Chromium.
5. Executes the Pytest test suite.

The workflow runs on GitHub-hosted Ubuntu runners and provides an automated validation process whenever code changes are submitted.

**Build status:** See the Playwright Tests badge at the top of this README.s
# Selenium Python Hybrid Automation Framework

A robust, scalable test automation framework built using Python and Selenium WebDriver. This project implements a **Hybrid approach**, combining the **Page Object Model (POM)** design pattern with **Data-Driven Testing (DDT)** to ensure maximum maintainability, reusability, and test coverage.

## 🚀 Key Features

*   **Page Object Model (POM):** Strict separation of web element locators and test execution logic.
*   **Data-Driven Testing (DDT):** Test data is managed externally using Excel spreadsheets (`selenium ddt.xlsx`), processed via custom utility scripts.
*   **Pytest Integration:** Utilizes `conftest.py` for efficient fixture management, setup, and teardown operations across the test suite.
*   **Automated Reporting:** Generates comprehensive HTML test execution reports with custom CSS styling.
*   **Failure Management:** Automatically captures and logs screenshots for failed test cases to streamline debugging.

## 📁 Project Structure

The repository is logically separated into distinct modules:

```text
Hybrid/
├── Pages/                  # Page classes containing locators and action methods (e.g., LoginPage.py)
├── Reports/                # Generated HTML execution reports and custom assets
├── ScreenShots/            # Automatically saved screenshots of test failures (e.g., fail.png)
├── Test data/              # External data files for DDT (e.g., selenium ddt.xlsx)
├── Tests/                  # Pytest test cases (e.g., test_login.py) and conftest.py
└── Utilities/              # Helper modules and reusable functions (e.g., excel_reader.py)

# Playwright Python POM Tests

This project contains Playwright (Python) tests using the Page Object Model (POM) for the site https://automationintesting.online/.
The test suite includes end-to-end flows such as booking/reservation, admin login/report checks, and related validation tests.

## Project Structure

Playwright_Python/
├── pages/                      # Page Object Model classes
│   ├── base_page.py
│   ├── home_page.py
│   ├── admin_page.py
│   ├── room_page.py
│   └── admin_report_page.py
├── tests/                      # pytest test modules
│   ├── test_reservation.py
│   └── test_admin_login.py
├── payload.json                # Test data / booking payload
├── invalid_passwords.json      # Passwords for negative tests
├── requirements.txt            # Python dependencies
├── pytest.ini                  # Pytest configuration
├── README.md                   # (this file)
└── .gitignore

## Technologies & Tools Used

Python 3.8+ (recommended 3.10–3.12)
Playwright for Python — browser automation
pytest — test runner
Page Object Model (POM) — test architecture / maintainability
Optionally:
pytest-xdist for parallel execution
pytest-html or --junitxml for re

## Requirements (example requirements.txt)

playwright==1.40.0
pytest==8.3.3
pytest-playwright==0.6.2
# optional
pytest-xdist
pytest-html
python-dateutil

## Setup — Windows

1. Clone the repo
git clone https://github.com/AllaKh/Playwright_Python.git
cd Playwright_Python

2. Create and activate a virtual environment
python -m venv .venv
# activate
.venv\Scripts\activate

3. Install Python dependencies
If requirements.txt exists:
pip install -r requirements.txt

If not, at minimum install Playwright + pytest:
pip install playwright pytest

4. Install browser binaries for Playwright
python -m playwright install
This downloads Chromium, Firefox, and WebKit browser engines required by Playwright.

## Setup — Linux / macOS

1. Clone the repo
git clone https://github.com/AllaKh/Playwright_Python.git
cd Playwright_Python

2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt
# or minimal
pip install playwright pytest

4. Install Playwright browsers
python -m playwright install

On some Linux distributions you may need extra system packages for browsers; Playwright will warn you if something is missing.

## How to run tests

Open a terminal with your virtualenv activated and run:
Run all tests in repository:
pytest

Run tests with verbose output:
pytest -v

Run one specific test file:
pytest tests/test_reservation.py -q

Run a single test function in a file:
pytest tests/test_reservation.py::test_full_reservation_flow -q

Stop on first failure:
pytest -x

Run tests in parallel (optional; requires pytest-xdist):
pytest -n auto

Generate HTML report (requires pytest-html):
pytest --html=report.html

Generate JUnit XML:
pytest --junitxml=report.xml


# Demoblaze Test Automation Project

This project is for automating tests on:
[https://www.demoblaze.com](https://www.demoblaze.com)

It uses:

* Python
* Selenium
* Pytest
* Page Object Model (POM)

---

## Project Structure

```
demoblaze/

├── conftest.py          # Browser setup
├── pytest.ini           # Pytest settings
├── requirements.txt     # Required packages

├── pages/               # Page classes (POM)
│   ├── base_page.py
│   ├── home_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── contact_page.py
│   └── about_page.py

├── tests/               # Test cases
│   ├── test_homepage.py
│   ├── test_signup.py
│   ├── test_login_logout.py
│   ├── test_product_page.py
│   ├── test_cart_page.py
│   ├── test_about_us.py
│   └── test_contact_page.py

└── reports/             # Test reports
```

---

## Setup

Install requirements:

```
pip install -r requirements.txt
```

Create reports folder:

```
mkdir reports
```

---

## Run Tests

Run all tests:

```
pytest
```

Run one file:

```
pytest tests/test_login_logout.py
```

Run one test:

```
pytest tests/test_login_logout.py::TestLoginLogout::test_LP_05_login_with_valid_credentials
```

Show logs:

```
pytest -s
```

Headless mode (no browser UI):
Enable this in `conftest.py`:

```
options.add_argument("--headless=new")
```

---

## Test Report

After running tests, open:

```
reports/report.html
```

---

## Login Details

```
Username: testsme
Password: test123
```

---

## What is POM?

POM means:

* pages/ = actions (click, login, etc.)
* tests/ = test cases only

Example:

```
page.login("user", "pass")
```

---


# 🛒 Demoblaze E-commerce QA Automation Project

This repository contains a QA testing project for the [Demoblaze](https://www.demoblaze.com/) demo e-commerce website. The project includes a complete **manual and automated testing framework** using Python, Selenium, and Pytest, alongside professional documentation (STP & STD).

---

## 📌 Project Objective

To validate the core functionalities of the Demoblaze website including:
- Authentication (Login/Signup)
- Product listing and navigation
- Shopping cart behavior
- Checkout and purchase flow
- UI responsiveness and carousel behavior

---

## 📁 Project Structure
```
demoblaze_project/
├── pages/                   # Page Object Model for all pages
│   ├── login_page.py
│   ├── signup_page.py
│   ├── products_page.py
│   └── cart_page.py
│
├── tests/                   # All test suites organized by functionality
│   ├── test_login.py
│   ├── test_signup.py
│   ├── test_products.py
│   └── test_cart.py
│
├── conftest.py              # Pytest fixture for WebDriver
├── STP.docx                 # Software Test Plan
├── STD.docx                 # Software Test Design
├── requirements.txt         # Python dependencies
└── README.md
```

---

## ✅ Test Coverage Summary

### `test_login.py`
- `test_login_success`
- `test_login_failure`
- `test_login_success_weak_password_username`

### `test_signup.py`
- `test_signup_success`

### `test_products.py`
- `test_products_displayed`
- `test_carousel_all_indicators_change_image`
- `test_click_product_opens_details`
- `test_click_product_opens_details_from_next_page`
- `test_add_to_cart`

### `test_cart.py`
- `test_buy_with_fully_details`
- `test_buy_with_empty_details` ⚠️ *Expected to fail – site accepts empty fields (Bug)*
- `test_buy_without_login` ⚠️ *Expected to fail – site allows purchase without login (Bug)*

---

## 📄 Documentation

| Document | Description |
|----------|-------------|
| `STP.docx` | Software Test Plan – defines scope, objectives, test types, environment, tools |
| `STD.docx` | Software Test Design – contains detailed test cases, preconditions, expected results |
| Bug Report | Embedded as comments and expectations in test scripts |

---

## 🧪 Tools & Environment

- **Language**: Python
- **Frameworks**: Selenium, Pytest
- **Browser Tested**: Edge, Chrome
- **Devices**: Windows 11 Desktop, iPhone 11 (Responsive)
- **Other Tools**: WebDriverManager, Allure (optional for reporting)

---

## 🧰 How to Run Tests

1. **Install requirements:**
   ```bash
   pip install -r requirements.txt



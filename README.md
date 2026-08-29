# Hidr_Application
# 📌 Project Overview

<div align="justify">

**HIDR Automation** is an automated testing framework developed to test the **HIDR Nepal website** using **Python, Selenium WebDriver, and Pytest**.

The project follows the **Page Object Model (POM)** design pattern to keep locators, page actions, test cases, and reusable utilities organized, maintainable, and scalable.

**Website:** https://hidr.com.np/

The framework is designed to support **functional testing, navigation testing, UI validation, regression testing, cross-browser testing, broken-link checking**, and other web application quality checks.

</div>

---

# 🎯 Project Objectives

<div align="justify">

The main objectives of this automation project are to:

</div>

* ✅ Automate important HIDR website user workflows.
* ✅ Validate website functionality and navigation.
* ✅ Verify UI elements and page behavior.
* ✅ Reduce repetitive manual testing.
* ✅ Detect broken links and invalid URLs.
* ✅ Support reusable and maintainable test scripts.
* ✅ Execute automated tests with Pytest.
* ✅ Support cross-browser testing.
* ✅ Generate test execution reports.
* ✅ Follow a scalable **Page Object Model (POM)** architecture.

---

# 🛠️ Technologies & Tools

| Technology / Tool                | Purpose                         |
| -------------------------------- | ------------------------------- |
| 🐍 **Python**                    | Programming language            |
| 🌐 **Selenium WebDriver**        | Browser automation              |
| 🧪 **Pytest**                    | Test framework                  |
| 🏗️ **Page Object Model (POM)**  | Test architecture               |
| ⏱️ **WebDriverWait**             | Explicit synchronization        |
| 🔗 **Requests**                  | HTTP and broken-link validation |
| 🌐 **Google Chrome**             | Browser testing                 |
| 🦊 **Firefox**                   | Browser testing                 |
| 🌐 **Microsoft Edge / Chromium** | Cross-browser testing           |
| 📦 **Git**                       | Version control                 |
| 🐙 **GitHub**                    | Source code management          |
| 💻 **PyCharm**                   | Development environment         |

---

## 🚀 Testing Coverage

<div align="justify">

The HIDR Automation framework provides comprehensive automated testing coverage for the HIDR Nepal website. It is structured to make test cases reusable, readable, and easy to maintain as the application grows.

</div>

* 🔹 Functional Testing
* 🔹 Navigation Testing
* 🔹 UI Validation
* 🔹 Regression Testing
* 🔹 Cross-Browser Testing
* 🔹 Broken Link Testing
* 🔹 Page Validation
* 🔹 Workflow Testing
* 🔹 Automated Test Execution
* 🔹 Test Reporting

---

## 🏗️ Framework Architecture

```text
HIDR-Automation/
│
├── pages/
│   ├── home.py
│   ├── opportunity.py
│   ├── publication.py
│   └── ...
│
├── tests/
│   ├── test_home.py
│   ├── test_opportunity.py
│   ├── test_publication.py
│   └── ...
│
├── utils/
│   ├── driver_factory.py
│   └── ...
│
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## ▶️ How to Run the Project

```bash
# Clone the repository
git clone <your-github-repository-url>

# Navigate to the project
cd HIDR-Automation

# Create virtual environment
python -m venv venv

# Activate virtual environment - Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run tests with verbose output
pytest -v
```

---

## 📊 Test Reporting

<div align="justify">

The framework can be integrated with test reporting tools such as **Allure Report** to provide detailed information about test execution, test status, failures, and execution history.

</div>

```bash
pytest --alluredir=allure-results
```

Generate the Allure report:

```bash
allure serve allure-results
```

---

## 🌐 Cross-Browser Testing

<div align="justify">

The framework is designed to support testing across multiple browsers to ensure consistent functionality and user experience.

</div>

| Browser                   | Supported |
| ------------------------- | --------- |
| Chrome                    | ✅         |
| Firefox                   | ✅         |
| Microsoft Edge / Chromium | ✅         |

---

## 👨‍💻 Author

**Abinash Malla Thakuri**

**Role:** Software Developer / QA Automation Tester

---

## 📄 License

This project is created for **software testing, automation practice, and quality assurance purposes**.

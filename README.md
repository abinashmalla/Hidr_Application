# Hidr_Application
# 🚀 HIDR E2E & Complete Workflow Automation

## 📌 Project Overview

**HIDR E2E & Complete Workflow Automation** is an automated testing project developed to validate the complete end-to-end workflow of the **HIDR Nepal website**. The project focuses on simulating real user journeys across multiple modules and verifying that the complete application workflow functions correctly from start to finish.

The automation framework is built using **Python, Selenium WebDriver, and Pytest**, following the **Page Object Model (POM)** design pattern to ensure the test code is reusable, maintainable, scalable, and easy to manage.

**Website:** https://hidr.com.np/

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Validate complete end-to-end user workflows.
* Verify navigation between different HIDR modules and pages.
* Validate user interactions and business workflows.
* Identify functional and integration issues across the application.
* Reduce repetitive manual testing through automation.
* Improve regression testing efficiency.
* Ensure consistent application behavior across critical workflows.

---

## 🧪 Testing Scope

The project covers complete workflows across key HIDR website modules, including:

* 🏠 Home Page
* 💼 Opportunities
* 👥 Careers
* 🤝 Partnership
* 📰 Publications / Blog
* 📚 Reports
* 📄 Policy Briefs
* 🖼️ Gallery
* 📞 Contact Us
* 🔗 Internal Page Navigation
* 🔄 Complete End-to-End User Journeys

---

## 🔄 E2E Workflow

The automation validates a complete user journey by performing a sequence of actions across the application:

```text
Launch HIDR Website
        ↓
Home Page Validation
        ↓
Navigate Through Main Sections
        ↓
Explore Opportunities
        ↓
Validate Career / Partnership Sections
        ↓
Navigate Publications & Reports
        ↓
Validate Blog / Policy Briefs
        ↓
Validate Gallery
        ↓
Navigate to Contact Section
        ↓
Validate Complete User Journey
        ↓
Verify Expected Results
        ↓
Test Completed Successfully
```

---

## 🛠️ Technologies & Tools

| Technology / Tool           | Purpose                                |
| --------------------------- | -------------------------------------- |
| **Python**                  | Automation programming language        |
| **Selenium WebDriver**      | Browser automation                     |
| **Pytest**                  | Test execution and test framework      |
| **Page Object Model (POM)** | Maintainable test architecture         |
| **WebDriverWait**           | Explicit synchronization               |
| **Git & GitHub**            | Version control and project management |
| **Allure**                  | Test reporting                         |
| **Chrome / Firefox / Edge** | Cross-browser testing                  |

---

## 📂 Project Structure

```text
HIDR_Workflow/
│
├── pages/
│   ├── home_page.py
│   ├── opportunity_page.py
│   ├── publication_page.py
│   ├── career_page.py
│   └── contact_page.py
│
├── tests/
│   ├── test_home.py
│   ├── test_opportunity.py
│   ├── test_publication.py
│   ├── test_career.py
│   └── test_e2e_workflow.py
│
├── utils/
│   └── driver_factory.py
│
├── screenshots/
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ⚙️ Key Automation Features

### ✅ Page Object Model

Each application page is represented by a dedicated Page Object class containing:

* Web element locators
* Page actions
* Reusable methods
* Navigation functions

This separates test logic from UI implementation and improves maintainability.

### ✅ Explicit Waits

The framework uses Selenium explicit waits to synchronize test execution with dynamic web elements instead of relying heavily on fixed delays.

Example:

```python
WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(locator)
)
```

### ✅ End-to-End Validation

The E2E tests validate complete user workflows rather than testing individual pages in isolation.

### ✅ Reusable Test Components

Common browser actions and utilities are centralized to reduce code duplication.

### ✅ Cross-Browser Support

The framework can be configured to execute tests against multiple browsers such as:

```text
Chrome
Firefox
Edge
```

### ✅ Test Reporting

Test execution can be integrated with **Allure Reports** to provide detailed execution results and debugging information.

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the project

```bash
cd HIDR_Workflow
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run all tests

```bash
pytest
```

### 7. Run the E2E workflow

```bash
pytest tests/test_e2e_workflow.py -v
```

### 8. Run tests with detailed output

```bash
pytest -v -s
```

---

## 📊 Test Execution

The E2E workflow validates:

```text
✔ Page accessibility
✔ Navigation
✔ Element visibility
✔ Button interactions
✔ Dropdown interactions
✔ Link navigation
✔ Content loading
✔ User workflow
✔ Expected page behavior
✔ End-to-end application flow
```

---

## 🐛 Defect & Issue Tracking

During testing, identified issues can be documented with:

* Bug title
* Environment
* Steps to reproduce
* Expected result
* Actual result
* Severity
* Priority
* Screenshots / evidence
* Test case reference

Issues can be tracked using **Jira** or GitHub Issues.

---

## 📈 Benefits of the Automation

This project provides several benefits:

* Faster regression testing
* Reduced manual testing effort
* Improved test consistency
* Early identification of functional defects
* Better test coverage
* Reusable automation components
* Maintainable test architecture
* Improved confidence in application releases

---

## 🎯 Future Improvements

Planned improvements include:

* Integration with CI/CD pipelines
* Parallel test execution
* Extended cross-browser testing
* API and UI workflow integration
* Advanced Allure reporting
* Screenshot and video capture on failures
* Data-driven testing
* Automated regression suite
* Environment-based configuration

---

## 👨‍💻 Project Focus

**Testing Approach:**

```text
Manual Testing
      ↓
Test Case Design
      ↓
Automation Development
      ↓
Page Object Model
      ↓
End-to-End Testing
      ↓
Regression Testing
      ↓
Cross-Browser Testing
      ↓
Test Reporting
```

---

## 📌 Conclusion

The **HIDR E2E & Complete Workflow Automation** project demonstrates a structured approach to automating real-world application workflows using **Python, Selenium WebDriver, and Pytest**.

By implementing the **Page Object Model**, explicit waits, reusable utilities, and end-to-end workflow validation, the project provides a scalable foundation for functional and regression testing of the HIDR Nepal website.

**Project Type:** End-to-End & Complete Workflow Automation
**Framework:** Selenium + Pytest
**Language:** Python
**Design Pattern:** Page Object Model (POM)
**Application:** HIDR Nepal Website
Automation Project

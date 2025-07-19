# 🧪 OrangeHRM UI Test Automation (Selenium + PyTest)

Automated UI test suite for the [OrangeHRM demo site](https://opensource-demo.orangehrmlive.com/), developed as part of a QA automation technical assessment.

This project validates key user workflows including login, employee management, and logout — using Selenium WebDriver and PyTest, structured with the Page Object Model (POM).

---

## 🔧 Tech Stack

- **Language**: Python 3.x
- **Framework**: PyTest
- **Automation**: Selenium WebDriver
- **Driver Management**: WebDriver Manager
- **Environment Support**: python-dotenv (optional)

---

## ✅ Test Scenarios

1. **Login Test**
   - Log in with valid credentials (`Admin / admin123`)
   - Assert successful login by checking dashboard visibility

2. **Add New Employee**
   - Navigate to PIM > Add Employee
   - Fill in employee name and ID
   - Assert redirect to Personal Details page and success message

3. **Search for Employee**
   - Navigate to PIM > Employee List
   - Search by name or ID
   - Assert presence of employee in result list

4. **Update Personal Details**
   - Edit nationality and birthdate
   - Assert updated fields are saved and correctly displayed

5. **Logout Flow**
   - Click top-right user menu
   - Select "Logout"
   - Assert redirection to login page

---

## 📁 Project Structure

<pre> . ├── pages/ # Page Object classes │   └── ... ├── tests/ # Test files for each scenario │   └── ... ├── utils/ # Reusable utilities (e.g., waits) ├── conftest.py # PyTest setup/teardown fixtures ├── requirements.txt # Project dependencies ├── pytest.ini # PyTest config (verbosity, paths) └── README.md # Project overview (this file) </pre>

---

## 🚀 Getting Started

1. Clone the Repo
'''
git clone https://github.com/vinimj18/Selenium_Python.git
cd Selenium_Python
'''

2. Install Dependencies
'''bash
Copy
Edit
pip install -r requirements.txt
'''


''''3. Run All Tests
bash
Copy
Edit
pytest
'''

## ⚙️ Configuration
Tests run directly against the public OrangeHRM demo site

ChromeDriver is automatically managed using webdriver-manager

You can optionally add a .env file for future credential storage (not required for this demo)

## 📌 Assumptions & Known Limitations
The OrangeHRM demo resets frequently, so created employee records may disappear between test runs

Date selection for birthdate uses direct input due to inconsistent calendar widget behavior

No test data is persisted; each run starts clean

## 👤 Author
Vinicius Maggiotto Justen
📍 Lisbon, Portugal
📧 viniciusmaggiotto@gmail.com
🔗 GitHub ・ LinkedIn


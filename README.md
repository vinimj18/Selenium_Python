# OrangeHRM UI Tests – Cypress + JavaScript

This branch contains end-to-end UI test automation for the OrangeHRM application, built with [Cypress](https://www.cypress.io/) using JavaScript.

---

## 🔧 Tech Stack

- [Cypress](https://www.cypress.io/) – Test framework and runner
- JavaScript (ES6+)
- Node.js (npm for dependency management)

---

## 📁 Project Structure

```
.
├── cypress/
│   ├── e2e/                 # Test cases
│   ├── fixtures/            # Test data (JSON)
│   ├── support/             # Custom commands & setup
├── cypress.config.js        # Cypress configuration
├── package.json             # Node dependencies and scripts
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
npm install
```

### 2. Open Cypress Test Runner

```bash
npx cypress open
```

Click on E2E Testing  
Choose a browser  
Click on the Specs to run the tests

### 3. Run tests in headless mode

```bash
npx cypress run
```

---

## ✅ Available Test Cases

| Test Suite        | Description                           |
| ----------------- | ------------------------------------- |
| `login_logout`    | Login and logout flow                 |
| `create_employee` | Create new employee and validate flow |

---

## 🧪 Custom Commands

Common actions like `login` and `createNewEmployee` are abstracted into Cypress custom commands, located in:

```
cypress/support/commands.js
```

---

## 🌱 Branch Info

This is a parallel implementation of the OrangeHRM UI automation tests using **Cypress + JavaScript**, aligned with the original [`main` branch`](https://github.com/vinimj18/orangehrm-ui-tests) (Selenium + Python).

---

## 📌 Notes

- This project uses **fixtures** to manage test data (`login.json`).
- Test assertions include **URL checks** and **DOM element validation**.

---

## 👨‍💻 Author

**Vinicius Maggiotto Justen**  
[LinkedIn](https://www.linkedin.com/in/viniciusmaggiotto/)

/// <reference types="cypress" />

describe("login_logout", () => {
  before(function () {
    cy.fixture("login").then((t) => {
      this.testData = t;
    });

    // This will ignore an API call error that doesn't affect the functionality
    Cypress.on("uncaught:exception", (err) => {
      if (
        err.message.includes(
          "Cannot read properties of undefined (reading 'response')"
        )
      ) {
        return false;
      }
    });
  });

  context("login", function () {
    it("Successful login", function () {
      const loginInfo = this.testData.login;

      // Execute Login Steps
      cy.login(loginInfo);

      // Verify if elements in the dashboard are loaded correctly
      // Heade
      cy.get(".oxd-topbar-header-title").should("be.visible");
      // Main Menu
      cy.get(".oxd-main-menu").should("be.visible");
      // Dashboard Card
      cy.get(".orangehrm-dashboard-widget").should("be.visible");
    });
  });

  context("logout", function () {
    it("Successful logout", function () {
      const loginInfo = this.testData.login;
      // Execute Login and Logout steps
      cy.login(loginInfo);
      cy.logout(loginInfo);

      // Verify if login button is visible after logout
      cy.get(".orangehrm-login-button").should("be.visible");
    });
  });
});

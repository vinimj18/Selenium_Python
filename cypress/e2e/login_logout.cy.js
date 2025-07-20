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

      cy.login(loginInfo);

      cy.get(".oxd-topbar-header-title").should("be.visible");
      cy.get(".oxd-main-menu").should("be.visible");
      cy.get(".orangehrm-dashboard-widget").should("be.visible");
    });
  });

  context("logout", function () {
    it("Successful logout", function () {
      const loginInfo = this.testData.login;
      cy.login(loginInfo);

      cy.get(".oxd-userdropdown-icon").click();
      cy.get(".oxd-userdropdown-link").eq(3).click();

      cy.get(".orangehrm-login-button").should("be.visible");
    });
  });
});

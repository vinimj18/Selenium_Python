/// <reference types="cypress" />

describe("create employee", () => {
  before(function () {
    cy.fixture("login").then((t) => {
      this.testData = t;
    });
  });
  context("employee", function () {
    it("Create New Employee Successfully", function () {
      const loginInfo = this.testData.login;
      const employee = this.testData.newEmployee;

      cy.login(loginInfo);
      cy.createNewEmployee(employee);

      //   Asserts the correct url is loaded after creation
      cy.url({ timeout: 10000 }).should("include", "PersonalDetails");

      //   Asserts the new employee has the correct name
      cy.get(".oxd-text.oxd-text--h6.--strong").should(
        "have.text",
        `${employee.firstName} ${employee.lastName}`
      );
    });
  });
});

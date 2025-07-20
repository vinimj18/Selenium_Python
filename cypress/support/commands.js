// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
// Custom Commands names are self descriptive
Cypress.Commands.add("login", (loginInfo = "") => {
  cy.visit("/");

  cy.get('[name="username"]').type(loginInfo.username);
  cy.get('[name="password"]').type(loginInfo.password);

  cy.get(".orangehrm-login-button").click();
});

Cypress.Commands.add("logout", () => {
  cy.get(".oxd-userdropdown-icon").click();
  cy.get(".oxd-userdropdown-link").eq(3).click();
});

Cypress.Commands.add("createNewEmployee", (employee = "") => {
  cy.get(".oxd-main-menu-item").eq(1).click();
  cy.get(".oxd-topbar-body-nav-tab-item").eq(2).click();
  cy.get('[name="firstName"]').type(employee.firstName);
  cy.get('[name="lastName"]').type(employee.lastName);
  cy.get("button[type='submit']").click();
});

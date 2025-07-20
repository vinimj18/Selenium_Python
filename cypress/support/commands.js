// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************

Cypress.Commands.add("login", (loginInfo = "") => {
  cy.visit("https://opensource-demo.orangehrmlive.com/");

  cy.get('[name="username"]').type(loginInfo.username);
  cy.get('[name="password"]').type(loginInfo.password);

  cy.get(".orangehrm-login-button").click();
});

Cypress.Commands.add("logout", () => {
  cy.get(".oxd-userdropdown-icon").click();
  cy.get(".oxd-userdropdown-link").eq(3).click();
});

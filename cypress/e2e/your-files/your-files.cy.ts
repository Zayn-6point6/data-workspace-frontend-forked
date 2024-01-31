describe("Your files list view", () => {
    beforeEach(() => {
      cy.intercept("GET", "http://data-workspace-localstack:4566/notebooks.dataworkspace.local*", {fixture: "your-files/buckets-response.xml"})
      cy.intercept("GET", "/api/v1/aws_credentials", {fixture: "your-files/credentials-response.xml"})
      cy.visit("/files/");
    });
  
    it("should order the files descending by default", () => {
      cy.get("tr:contains('second_test_file.rtf')")
        .should('exist')
        .find("a")
        .should('have.text', 'second_test_file.rtf');

      cy.get("tr:contains('second_test_file.rtf')")
        .next("tr")
        .find("a")
        .should('have.text', 'third_test_file.rtf');

      cy.get("tr:contains('second_test_file.rtf')")
        .next("tr")
        .next("tr")
        .find("a")
        .should('have.text', 'test_file.rtf');
    });
  });
  
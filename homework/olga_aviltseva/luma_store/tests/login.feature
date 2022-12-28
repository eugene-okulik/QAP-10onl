Feature: Login page

    Scenario: email field is validated
    Given I am on a login page
    When I enter abrakadabra into email field
    And I enter valid password
    And I click Send button
    Then I see validation error


    Scenario: incorrect login alert
    Given I am on a login page
    When I enter non-existing user email into email field
    And I enter valid password
    And I click Send button
    Then I see alert message

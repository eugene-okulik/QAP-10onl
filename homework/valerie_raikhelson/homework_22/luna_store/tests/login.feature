Feature: Login page

    Scenario: email field is validated
        Given I am on a login page
        When I enter "aaa" into email field
        And I enter valid password
        And I click Send button
        Then I see validation error

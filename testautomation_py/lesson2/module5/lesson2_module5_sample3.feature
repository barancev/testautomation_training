Scenario: File Creation
    Given A directory
    And A valid <file_name>
    When I create a file with this name in the given directory
    Then I should see the file created successfully

    Examples:
    | file_name |
    | test.txt  |
    | .txt      |
    | @#$%^&    |

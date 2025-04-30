User Story: Reverse a String
Title: Reverse a String for Display Purposes

As a user,
I want to reverse a given string,
So that I can display it in reverse order for specific use cases like debugging, formatting, or creative text manipulation.

Acceptance Criteria:
The system should accept a string as input.
The system should return the reversed version of the string.
The system should handle edge cases, such as:
Empty strings.
Single-character strings.
Strings with spaces or special characters.
Palindromes (strings that are the same when reversed).
The system should log the original and reversed strings for traceability.
Unit tests should verify the functionality for various scenarios.
Example Scenarios:
Given: The input string is "hello".
When: The reverse function is called.
Then: The output should be "olleh".

Given: The input string is an empty string "".
When: The reverse function is called.
Then: The output should be "".

Given: The input string is "madam".
When: The reverse function is called.
Then: The output should be "madam" (same as input).

Given: The input string is "hello world".
When: The reverse function is called.
Then: The output should be "dlrow olleh".

Notes:
The feature is implemented in both Python and Java, ensuring cross-platform compatibility.
Unit tests are provided to validate the functionality in Python.
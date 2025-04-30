def reverse_string(s):
    # This function reverses the input string by inserting each character at the beginning of a list
    result = []
    for char in s:
        # Insert each character at the start of the list
        result.insert(0, char)
    # Join the list into a single string and return the reversed string
    return ''.join(result)

# Example usage
input_str = "hello"  # Input string to be reversed
reversed_str = reverse_string(input_str)  # Call the function to reverse the string
print(reversed_str)  # Print the reversed string
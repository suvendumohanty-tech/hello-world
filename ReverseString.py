def reverse_string(s):
    result = []
    for char in s:
        result.insert(0, char)
    return ''.join(result)

# Example usage
input_str = "hello"
reversed_str = reverse_string(input_str)
print(reversed_str)
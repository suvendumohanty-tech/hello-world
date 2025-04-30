#configure logging
import logging
# Set up logging configuration to display messages with timestamps
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def reverse_string(s):
    # This function takes a string as input and returns its reverse using slicing
    return s[::-1]

# Example usage
if __name__ == "__main__":
    # Test the reverse_string function with a sample string
    text = "hello world"
    # Print the reversed string to the console
    print("Reversed string:", reverse_string(text))
    # Log the reversed string for debugging purposes
    logging.info("Logging reversed string for debugging: %s", reverse_string(text))
    # Log the length of the original string
    logging.info("Length of the original string: %d", len(text))
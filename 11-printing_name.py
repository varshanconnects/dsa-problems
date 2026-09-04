# Printing Name
# Problem: Write a function that takes a name and returns a greeting message.
# Example: If the input is "Alice", the output should be "Hello, Alice!"
# Time Complexity: O(1)
# Space Complexity: O(1)


def print_name(name):
    """
    Args:
        name: A string containing a person's name

    Returns:
        A greeting string
    """
    return f"Hello, {name}!"


# Test cases
if __name__ == "__main__":
    print(print_name("Alice"))   # Hello, Alice!
    print(print_name("Bob"))     # Hello, Bob!
    print(print_name("Charlie"))  # Hello, Charlie!

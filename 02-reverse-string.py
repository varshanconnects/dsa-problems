# Reverse String
# Problem: Write a function that reverses a string.
# Time Complexity: O(n)
# Space Complexity: O(1) or O(n) depending on whether in-place is allowed

def reverseString(s):
    """
    Reverse a string using two pointers.
    
    Args:
        s: String to reverse
    
    Returns:
        Reversed string
    """
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

# Alternative solution using slicing
def reverseStringSlice(s):
    return s[::-1]

# Test cases
if __name__ == "__main__":
    print(reverseString("hello"))      # olleh
    print(reverseString("a"))          # a
    print(reverseString("ab"))         # ba
    print(reverseStringSlice("hello")) # olleh

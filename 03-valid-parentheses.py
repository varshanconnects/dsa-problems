# Valid Parentheses
# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s):
    """
    Check if parentheses are valid.
    
    Args:
        s: String containing parentheses
    
    Returns:
        Boolean indicating if valid
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0

# Test cases
if __name__ == "__main__":
    print(isValid("()"))      # True
    print(isValid("()[]{}"))  # True
    print(isValid("("))       # False
    print(isValid("([)]"))    # False
    print(isValid("[]"))      # True

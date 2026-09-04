# Palindrome Check
# Problem: Determine whether a string is a palindrome, considering only alphanumeric characters
# and ignoring cases.
# Time Complexity: O(n)
# Space Complexity: O(1)

def isPalindrome(s):
    """
    Check if string is a palindrome.
    
    Args:
        s: String to check
    
    Returns:
        Boolean indicating if palindrome
    """
    # Filter alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Alternative two-pointer approach without extra space
def isPalindromeOptimized(s):
    """
    Check if palindrome using two pointers without creating new string.
    
    Args:
        s: String to check
    
    Returns:
        Boolean indicating if palindrome
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Test cases
if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(isPalindrome("race a car"))                       # False
    print(isPalindrome(" "))                                # True
    print(isPalindromeOptimized("A man, a plan, a canal: Panama"))  # True

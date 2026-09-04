# Contains Duplicate
# Problem: Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
# Time Complexity: O(n)
# Space Complexity: O(n)

def containsDuplicate(nums):
    """
    Check if array contains duplicate values.
    
    Args:
        nums: List of integers
    
    Returns:
        Boolean indicating if duplicates exist
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Alternative using set comparison
def containsDuplicateAlt(nums):
    return len(nums) != len(set(nums))

# Test cases
if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))       # True
    print(containsDuplicate([1, 2, 3, 4]))       # False
    print(containsDuplicate([99, 99]))           # True
    print(containsDuplicateAlt([1, 2, 3, 1]))    # True

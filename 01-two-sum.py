# Two Sum
# Problem: Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.
# You may assume that each input has exactly one solution, and you may not use the same element twice.
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    """
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test cases
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(twoSum([3, 2, 4], 6))       # [1, 2]
    print(twoSum([3, 3], 6))          # [0, 1]

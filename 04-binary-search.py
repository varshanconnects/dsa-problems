# Binary Search
# Problem: Given a sorted array of integers nums and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums. You must write an algorithm with O(log n) runtime complexity.
# Time Complexity: O(log n)
# Space Complexity: O(1)

def binarySearch(nums, target):
    """
    Search for target in sorted array.
    
    Args:
        nums: Sorted list of integers
        target: Target value
    
    Returns:
        Index of target or -1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test cases
if __name__ == "__main__":
    print(binarySearch([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(binarySearch([-1, 0, 3, 5, 9, 12], 13))  # -1
    print(binarySearch([5], 5))                     # 0
    print(binarySearch([-1, 0, 3, 5, 9, 12], 0))   # 1

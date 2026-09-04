# Remove Duplicates from Sorted Array
# Problem: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
# such that each unique element appears only once. Return the number of unique elements.
# Time Complexity: O(n)
# Space Complexity: O(1)

def removeDuplicates(nums):
    """
    Remove duplicates from sorted array in-place.
    
    Args:
        nums: Sorted list with possible duplicates
    
    Returns:
        Number of unique elements
    """
    if not nums:
        return 0
    
    k = 1  # First element is always unique
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    
    return k

# Test cases
if __name__ == "__main__":
    nums1 = [1, 1, 2]
    k1 = removeDuplicates(nums1)
    print(f"Count: {k1}, Array: {nums1[:k1]}")  # Count: 2, Array: [1, 2]
    
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = removeDuplicates(nums2)
    print(f"Count: {k2}, Array: {nums2[:k2]}")  # Count: 5, Array: [0, 1, 2, 3, 4]

# Maximum Subarray (Kadane's Algorithm)
# Problem: Given an integer array nums, find the subarray with the largest sum and return the sum.
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxSubarray(nums):
    """
    Find maximum sum subarray using Kadane's algorithm.
    
    Args:
        nums: List of integers
    
    Returns:
        Maximum subarray sum
    """
    max_sum = current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test cases
if __name__ == "__main__":
    print(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 ([4, -1, 2, 1])
    print(maxSubarray([5, 4, -1, 7, 8]))                 # 23 (entire array)
    print(maxSubarray([-2, -1]))                          # -1
    print(maxSubarray([1]))                               # 1

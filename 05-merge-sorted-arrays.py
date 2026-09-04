# Merge Sorted Arrays
# Problem: Merge two sorted arrays into one sorted array.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

def mergeSortedArrays(arr1, arr2):
    """
    Merge two sorted arrays.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
    
    Returns:
        Merged sorted array
    """
    result = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result

# Test cases
if __name__ == "__main__":
    print(mergeSortedArrays([1, 3, 5], [2, 4, 6]))        # [1, 2, 3, 4, 5, 6]
    print(mergeSortedArrays([0], [1]))                    # [0, 1]
    print(mergeSortedArrays([], [0, 1]))                  # [0, 1]
    print(mergeSortedArrays([1, 2, 3], [4, 5, 6]))        # [1, 2, 3, 4, 5, 6]

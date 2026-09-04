# Fibonacci Sequence
# Problem: Compute the n-th Fibonacci number where F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
# Time Complexity: O(n)
# Space Complexity: O(1) - iterative, O(n) - recursive with memoization

def fibonacciIterative(n):
    """
    Compute Fibonacci number iteratively.
    
    Args:
        n: Position in Fibonacci sequence
    
    Returns:
        n-th Fibonacci number
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

# Recursive with memoization
def fibonacciMemo(n, memo=None):
    """
    Compute Fibonacci number with memoization.
    
    Args:
        n: Position in Fibonacci sequence
        memo: Dictionary for caching results
    
    Returns:
        n-th Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo)
    return memo[n]

# Test cases
if __name__ == "__main__":
    print(fibonacciIterative(0))   # 0
    print(fibonacciIterative(5))   # 5
    print(fibonacciIterative(10))  # 55
    print(fibonacciMemo(10))       # 55

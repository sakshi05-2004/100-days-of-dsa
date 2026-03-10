"""
Day 33: Power of a Number using Recursion

Problem:
Compute x raised to the power n using recursion.

Approach:
- Base case: if n == 0 → return 1
- Otherwise return x * power(x, n-1)

Time Complexity: O(n)
Space Complexity: O(n)
"""

def power(x, n):

    if n == 0:
        return 1

    return x * power(x, n - 1)


# Test
print("Power:", power(2, 5))
"""
Day 32: Fibonacci using Recursion

Problem:
Find the nth Fibonacci number using recursion.

Approach:
- Base cases:
    F(0) = 0
    F(1) = 1
- Otherwise:
    F(n) = F(n-1) + F(n-2)

Time Complexity: O(2^n)
Space Complexity: O(n)
"""

def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Test
print("Fibonacci:", fibonacci(6))
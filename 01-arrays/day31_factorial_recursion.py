"""
Day 31: Factorial using Recursion

Problem:
Find factorial of a number using recursion.

Approach:
- If n is 0 or 1 → return 1
- Otherwise return n * factorial(n-1)

Time Complexity: O(n)
Space Complexity: O(n) due to recursion stack
"""

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Test
print("Factorial:", factorial(5))
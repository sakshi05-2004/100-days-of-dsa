"""
Day 96: Fibonacci using Dynamic Programming
"""

def fibonacci(n, memo={}):

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


# Test
n = 10

print("Fibonacci:", fibonacci(n))
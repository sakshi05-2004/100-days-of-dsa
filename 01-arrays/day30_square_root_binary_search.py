"""
Day 30: Square Root using Binary Search

Problem:
Find the integer square root of a number without using sqrt().

Approach:
- Use binary search
- Check mid * mid against x
- Narrow search range

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def integer_sqrt(x):

    if x < 2:
        return x

    left = 1
    right = x
    result = 0

    while left <= right:

        mid = (left + right) // 2

        if mid * mid == x:
            return mid

        elif mid * mid < x:
            result = mid
            left = mid + 1

        else:
            right = mid - 1

    return result


# Test
print("Square root:", integer_sqrt(16))
print("Square root:", integer_sqrt(10))
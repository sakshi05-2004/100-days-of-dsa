"""
Day 49: Next Greater Element using Stack
"""

def next_greater_element(arr):

    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):

        # Remove smaller elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack not empty, top is next greater
        if stack:
            result[i] = stack[-1]

        # Push current element
        stack.append(arr[i])

    return result


# Test
arr = [4, 5, 2, 10]
print("Next Greater Elements:", next_greater_element(arr))
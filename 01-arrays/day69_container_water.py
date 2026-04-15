"""
Day 69: Container With Most Water
"""

def max_area(height):

    left = 0
    right = len(height) - 1

    max_water = 0

    while left < right:

        area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, area)

        # Move smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Test
arr = [1,8,6,2,5,4,8,3,7]

print("Max Water:", max_area(arr))
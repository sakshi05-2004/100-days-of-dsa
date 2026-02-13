"""
Day 9: Best Time to Buy and Sell Stock

Problem:
Given stock prices by day, find the maximum profit
you can achieve with one buy and one sell.

Approach:
- Track minimum price so far
- Calculate profit at each step
- Keep updating maximum profit

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


# Test
prices = [7, 1, 5, 3, 6, 4]
print("Maximum Profit:", max_profit(prices))




# You are given an array prices where prices[i] is the price of a given stock on the i-th day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (buy one and sell one share of the stock multiple times).

# Example: prices = [7,1,5,3,6,4] Return: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

# Steps
# Define a function called 'buy_and_sell_stock'
# Initialize a variable to store your maximum profit. Start its value at 0.
# Loop through the list of 'prices', stopping before the last element.
# Compare the current price with the price of the next day.
# If the next day's price is higher, calculate the profit for this pair of days and add it to maximum profit.
# Return the value stored in 'maximum' as it contains the maximum profit you can achieve.

# Pre-code
def buy_and_sell_stock(prices):
    max_profit = 0

    for i in range(0, len(prices) - 1):
        if prices[i] < prices[i + 1]:
            max_profit += prices[i + 1] - prices[i]

    return max_profit

prices = [7,1,5,3,6,4]
print(f"Prices: {prices}")
print(f"Max Profit From Prices: {buy_and_sell_stock(prices)}")

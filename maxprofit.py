# Given an array prices[] of size N denoting the cost of stock on each day, 
# the task is to find the maximum total profit if we can buy and sell the stocks any number of times.
# Input: prices[] = {100, 180, 260, 310, 40, 535, 695}
# Output: 865
# Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
#                        Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
#                        Maximum Profit  = 210 + 655 = 865


def find_max_profit(prices):
    # Initialize maximum profit
    max_profit = 0
    
    # Loop through prices starting from the first day
    for i in range(1, len(prices)):
        # If today's price is higher than yesterday's, sell stock for profit
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    
    return max_profit

# Taking input from user
values = input("Enter the prices separated by spaces: ")
prices = list(map(int, values.split()))  # Convert input to list of integers

# Call the function and print the result
s = find_max_profit(prices)
print("Maximum Profit:", s)

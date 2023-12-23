def maxProfit(prices):
    l, r = 0, 1  # Initialize two pointers, l for buy and r for sell
    maxP = 0  # Max profit
    
    while r < len(prices):  # Iterate until r reaches the end of the list
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]  # Calculate potential profit
            print(f"Buying at {prices[l]} and selling at {prices[r]}, Profit: {profit}")
            maxP = max(maxP, profit)  # Update max profit if current profit is higher
        else:
            print(f"Price at {prices[l]} is not profitable, moving to {prices[r]}")
            l = r  # Move the buy pointer to the current sell position
        r += 1  # Move the sell pointer to the next day

    print(f"Maximum profit: {maxP}")
    return maxP

# Example usage:
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Expected output: 5 (buy at 1, sell at 6)

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    
    l, r = 0, 1 # left=buy, right=sell
    maxP = 0
    
    # while right pointer hasn't surpassed the length of prices
    while r < len(prices): 
        # check for profit
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
             l = r # move the left pointer to the right
        r += 1
    return maxP

# Example usage:
print(maxProfit([7, 1, 5, 3, 6, 4]))
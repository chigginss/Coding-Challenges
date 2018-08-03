
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # iterate through prices
        # if the value of one day is lower than the value on another day, return max           
        # profit - if this does not occur, return None

        profit = 0
        
        if len(prices) > 0:
            current_min = prices[0]
        
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - current_min)
            current_min = min(prices[i], current_min)

        return profit

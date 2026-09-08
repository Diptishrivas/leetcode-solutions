class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        for price in prices:

            buy = min(buy, price)

            current_profit = price - buy

            profit = max(profit, current_profit)

        return profit
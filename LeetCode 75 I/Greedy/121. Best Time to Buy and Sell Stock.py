class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_buy, p_sell, profit = 0, 1, 0
        while p_sell<len(prices):
            if prices[p_buy]<prices[p_sell]:
                c_profit = prices[p_sell] - prices[p_buy]
                profit = max(profit, c_profit)
            else:
                p_buy = p_sell
            p_sell += 1
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price_index = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[min_price_index]

            if profit > max_profit:
                max_profit = profit
            
            if prices[i] < prices[min_price_index]:
                min_price_index = i
        
        return max_profit
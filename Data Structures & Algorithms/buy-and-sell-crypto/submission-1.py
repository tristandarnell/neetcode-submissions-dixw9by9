class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        most_profit = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
            most_profit = max(most_profit, profit)
        return most_profit

            

        

        
    
            




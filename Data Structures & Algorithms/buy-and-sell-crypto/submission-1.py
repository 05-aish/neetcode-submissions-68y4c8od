class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        for j in range(1, len(prices)):
                if(prices[j] > prices[i]):
                        res = prices[j] - prices[i]
                        profit = max(profit, res)      
                else:
                        i = j

        return profit


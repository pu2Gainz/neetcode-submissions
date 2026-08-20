class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       maxProfit = 0
       minPrice = prices[0]
       for i in prices:
        minPrice = min(minPrice, i)
        maxProfit = max(maxProfit, i - minPrice)
    
       return  maxProfit
         
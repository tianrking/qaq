class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf') ## 无穷大  - 无穷小
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

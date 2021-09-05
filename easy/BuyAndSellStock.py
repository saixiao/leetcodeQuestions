class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        cheapestStonk = float("inf")
        
        for stockPrice in prices:
            cheapestStonk = min(cheapestStonk, stockPrice)
            maxProfit = max(maxProfit, stockPrice - cheapestStonk)
        
        return maxProfit
                
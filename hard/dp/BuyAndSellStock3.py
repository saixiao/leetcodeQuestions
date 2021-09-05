class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        money_after_first_buy = float("-inf")
        money_after_second_buy = float("-inf")
        money_after_first_sell = 0
        money_after_second_sell = 0
        
        for price in prices:
            money_after_second_sell = max(money_after_second_sell, price + money_after_second_buy)
            money_after_second_buy = max(money_after_second_buy, money_after_first_sell - price)
            money_after_first_sell = max(money_after_first_sell, money_after_first_buy + price)
            money_after_first_buy = max(money_after_first_buy, 0 - price)
        
        return money_after_second_sell
        
        
            
            
class Solution(object):
    def maxProfit(self, prices):
        minprice=prices[0]
        maxprofit=0
        for price in prices :
            minprice = min(minprice,price)
            profit=price-minprice
            maxprofit=max(maxprofit,profit)
        return maxprofit
        
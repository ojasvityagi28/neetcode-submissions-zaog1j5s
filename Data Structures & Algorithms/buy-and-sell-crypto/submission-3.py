class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini= 0
        maxprofit=0
        for i in range(1,len(prices)):
            if prices[i]< prices[mini] :
                mini =i
            maxprofit=max(maxprofit, prices[i]-prices[mini])
        
        for j in range(mini+1,len(prices)):
            maxprofit=max(maxprofit, prices[j]-prices[mini])
        return maxprofit

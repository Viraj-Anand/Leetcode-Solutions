class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_so_far=float('inf')
        currprofit=0
        profit=0

        for i in prices:
            if i<least_so_far:
                least_so_far=i
            currprofit=i-least_so_far
            if profit<currprofit:
                profit=currprofit

        return profit
        
        
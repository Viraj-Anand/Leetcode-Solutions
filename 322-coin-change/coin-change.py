class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def solve(index,rem):
            if rem==0:
                return 0
            if index>=n or rem<0:
                return float('inf')

            if (index,rem) in dp:
                return dp[(index,rem)]
            
            op1=1+solve(index,rem-coins[index])
            op2=solve(index+1,rem)
            dp[(index,rem)]=min(op1,op2)
            return dp[(index,rem)]
        dp={}
        n=len(coins)
        res=solve(0,amount)
        return res if res!=float('inf') else -1

        
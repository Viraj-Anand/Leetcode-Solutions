class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def solve(target,index):
            if index==target:
                return 1
            if index>target:
                return 0
            if index in dp:
                return dp[index]
            ans=0
            for i in nums:
                ans+=solve(target,index+i)
                dp[index]=ans

            return dp[index]

        dp={}
        return solve(target,0)
        
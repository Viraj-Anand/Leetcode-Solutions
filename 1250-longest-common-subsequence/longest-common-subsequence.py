class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def solve(i,j,a,b):
            if i==len(a) or j==len(b):
                return 0
            count=0
            if (i,j) in dp:
                return dp[(i,j)]

            if a[i]==b[j]:
                count=1+solve(i+1,j+1,a,b)
            else:
                count=max(solve(i+1,j,a,b),solve(i,j+1,a,b))
            dp[(i,j)]=count

            return dp[(i,j)]
        dp={}
        return solve(0,0,text1,text2)

        
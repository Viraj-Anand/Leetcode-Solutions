class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def solve(index, s, set):
            if index == n:
                return True
            temp = ''
            if index in dp:  # check if index is in dp
                return dp[index]
            
            for j in range(index, n):
                temp += s[j]
                if temp in set:
                    dp[index] = solve(j + 1, s, set)
                    if dp[index]:
                        return True
            return False

        dp = {}
        n = len(s)
        hashset = set(wordDict)
        return solve(0, s, hashset)

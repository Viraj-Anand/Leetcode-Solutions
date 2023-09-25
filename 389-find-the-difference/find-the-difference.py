class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        news=sorted(s)
        newt=sorted(t)

        for i in range(len(news)):
            if news[i]!=newt[i]:
                return newt[i]

        return newt[-1]
        
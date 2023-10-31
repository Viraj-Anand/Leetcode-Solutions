class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        maxlen=0
        for i in hashset:
            if i-1 not in hashset:
                curr=i
                length=1

                while curr+1 in hashset:
                    curr+=1
                    length+=1
                if length>maxlen:
                    maxlen=length

        return maxlen 

        
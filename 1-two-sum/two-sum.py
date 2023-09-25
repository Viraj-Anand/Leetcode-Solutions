class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dic={}
        for i in range(n):
            diff=target-nums[i]
            if nums[i] not in dic:
                dic[diff]=i
            else:
                return i,dic[nums[i]]
        
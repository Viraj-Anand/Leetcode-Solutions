class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in nums:
            index=abs(i)-1
            if nums[index]<0:
                res.append(index+1)
            else:
                nums[index]=-nums[index]

        for i in range(n):
            nums[i]=abs(nums[i])

        return res

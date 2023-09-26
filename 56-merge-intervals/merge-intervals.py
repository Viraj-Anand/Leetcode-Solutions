class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        arr=[]

        for i in intervals:
            if not arr or i[0]>arr[-1][1]:
                arr.append(i)
            arr[-1][1]=max(arr[-1][1],i[1])

        if arr[-1][1]<intervals[-1][1]:
            return -1

        return arr
        
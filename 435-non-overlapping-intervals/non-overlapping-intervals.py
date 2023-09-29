class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])

        count=0
        prev=intervals[0]

        for i in range(1,n):
            if intervals[i][0]<prev[1]:
                count+=1
            else:
                prev=intervals[i]

        return count


        
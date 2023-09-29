class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        count=0
        while points:
            end=points.pop(0)[1]
            count+=1
            while points and points[0][0]<=end:
                points.pop(0)

        return count

        
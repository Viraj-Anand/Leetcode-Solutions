class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m=len(firstList)
        n=len(secondList)
        i=0
        j=0
        res=[]
        while i<m and j<n:
            start=max(firstList[i][0],secondList[j][0]) # take the max of starting elemnts
            end=min(firstList[i][1],secondList[j][1]) # take the min of ending elements

            if start<=end: # if overlappping,append to result
                res.append([start,end])

            if firstList[i][1]<secondList[j][1]: # iterate through whihever list element is smaller
                i+=1
            else:
                j+=1

        return res
        

        
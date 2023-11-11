from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indeg=[0]*numCourses

        for i,j in prerequisites:
            graph[j].append(i)
            indeg[i]+=1

        q=[]
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)

        while q:
            node=q.pop(0)
            numCourses-=1

            for neighbor in graph[node]:
                indeg[neighbor]-=1
                if indeg[neighbor]==0:
                    q.append(neighbor)

        return numCourses==0

        
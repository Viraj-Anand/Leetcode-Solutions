from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph=defaultdict(list)
        indeg=[0]*numCourses

        for i,j in prerequisites:
            graph[j].append(i)
            indeg[i]+=1

        q=[]
        res=[]

        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)

        while q:
            node=q.pop(0)
            res.append(node)

            for neighbor in graph[node]:
                indeg[neighbor]-=1
                if indeg[neighbor]==0:
                    q.append(neighbor)

        if len(res)==numCourses:
            return res
        else:
            return []
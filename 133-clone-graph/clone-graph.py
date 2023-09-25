"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        dic={}

        def dfs(node):
            if node in dic:
                return dic[node]
            clone=Node(node.val,[])
            dic[node]=clone

            for i in node.neighbors:
                clone.neighbors.append(dfs(i))

            return clone

        return dfs(node) if node else None        
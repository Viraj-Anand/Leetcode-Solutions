# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        res=[]
        def inorder(res,node):
            if node.left:
                inorder(res,node.left)
            res.append(node.val)
            if node.right:
                inorder(res,node.right)

            return res

        res=inorder(res,root)
        return res[k-1]
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return same(p.left,q.left) and same(p.right,q.right)

        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
        return same(root,subroot) or self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val==p.val or root.val==q.val:
            return root

        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

    
        if left==None and right==None: #it means that neither p nor q are found in the current subtree
            return None
        if left==None and not right==None: # it means both p and q are found in the right subtree
            return right
        if not left==None and right==None: # it means both p and q are found in the left subtree
            return left
        if not left==None and not right==None: # if both left and right are not None, it means p and q are found in different subtree. so the current node "root" is the LCA
            return root

        
        

        
class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, node):
        if not node:
            return 0

        # max gain if we go through the left child
        left_gain = max(self.max_gain(node.left), 0)
        # max gain if we go through the right child
        right_gain = max(self.max_gain(node.right), 0)

        # the price to start a new path where `node` is the highest node
        new_path_price = node.val + left_gain + right_gain

        # update max_sum if it's better to start a new path
        self.max_sum = max(self.max_sum, new_path_price)

        # for recursion:
        # return the max gain if continue the same path
        return node.val + max(left_gain, right_gain)

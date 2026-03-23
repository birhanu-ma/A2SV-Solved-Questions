# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        def dfs(node, parent_val, gp_val):
            if not node:
                return
            
            if gp_val is not None and gp_val % 2 == 0:
                self.total_sum += node.val
            
            dfs(node.left, node.val, parent_val)
            dfs(node.right, node.val, parent_val)
            
        dfs(root, None, None)
        return self.total_sum

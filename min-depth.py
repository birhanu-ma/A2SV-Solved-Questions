# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0        
        self.min_len = float("inf")
        
        def helper(root, current_depth):
            if not root:
                return
            if not root.left and not root.right:
                self.min_len = min(self.min_len, current_depth)
                return
            
            helper(root.left, current_depth + 1)
            helper(root.right, current_depth + 1)
        helper(root, 1)
        return self.min_len

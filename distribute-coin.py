# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.cnr = 0
    def distributeCoins(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(root):
            if not root:
                return 0
            
            left_balance = helper(root.left)
            right_balance = helper(root.right)
  
            self.cnr += abs(left_balance) + abs(right_balance)
            
            balance = root.val + left_balance + right_balance - 1
            
            return balance

        helper(root)
        
        return self.cnr

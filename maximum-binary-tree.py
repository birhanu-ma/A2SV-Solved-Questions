# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        maximum = max(nums)
        root = TreeNode(maximum)
        root.right = self.constructMaximumBinaryTree(nums[nums.index(maximum)+1:])
        root.left = self.constructMaximumBinaryTree(nums[:nums.index(maximum)])
      
        return root



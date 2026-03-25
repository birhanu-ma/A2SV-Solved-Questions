# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ctr = defaultdict(int)
        self.ctr[0] = 1
        self.cnr = 0
        self.running_sum = 0
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def helper(root, targetSum):
            if root:
                self.running_sum+=root.val
                if self.ctr[self.running_sum-targetSum]!=0:
                    self.cnr+=int(self.ctr[self.running_sum-targetSum])
                self.ctr[self.running_sum]+=1
                helper(root.left, targetSum)
                helper(root.right,targetSum)
                self.ctr[self.running_sum]-=1
                self.running_sum-=root.val
        helper(root, targetSum)
        return self.cnr
        
            

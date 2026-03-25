# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.ctr = defaultdict(int)
   
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if root:
            if self.ctr[k-root.val]!=0:
                return True
            self.ctr[root.val]+=1
            return self.findTarget(root.left,k) or self.findTarget(root.right,k)
            
        else:
            return False
        self.findTarget(root, k)
            
        

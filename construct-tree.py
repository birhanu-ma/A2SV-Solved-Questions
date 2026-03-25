
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        preorder = deque(preorder)
        def build(preorder, postorder):
            if not postorder:
                return None
           
            if postorder:
                idx = postorder.index(preorder.popleft())
                root = TreeNode(postorder[idx])
                if len(postorder) == 1:
                    return root
                if postorder:
                    left_node_idx = postorder.index(preorder[0])
                root.left = build(preorder, postorder[:left_node_idx+1])
                root.right = build(preorder, postorder[left_node_idx+1:-1])
                return root
        return build(preorder, postorder)

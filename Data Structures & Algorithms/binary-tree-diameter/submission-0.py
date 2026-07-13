# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.diameter = 0
        def maxdepth(node):
            if node is None:
                return 0
            left_sub = maxdepth(node.left)
            right_sub = maxdepth(node.right)
            self.diameter = max(self.diameter , (left_sub + right_sub))
            return 1 + max(left_sub , right_sub)
        
        maxdepth(root)
        return self.diameter






        
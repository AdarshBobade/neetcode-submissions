# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return False
        def check(node):
            if node is None :
                return True

            if node.left and node.right :
                return (node.left.val < node.val and 
                        node.right.val > node.val)
            
            return check(node.left) and check(node.right)

        return check(root)







        
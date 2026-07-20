# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # using recursive inorder traversal
        def inorder(node , prev):
            
            if not node :
                return True , prev
            
            valid , prev = inorder(node.left , prev)

            if not valid :
                return False , prev
            if node.val <= prev :
                return False , prev

            prev = node.val
            return inorder(node.right , prev)

        valid , _ = inorder(root , prev = float("-infinity"))
        return valid
            






        
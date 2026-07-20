# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node , limit):
            if not node:
                return True
            
            if not limit[0] < node.val < limit[1] :
                return False
            
            left = check(node.left , [limit[0] , node.val])
            right = check(node.right , [node.val , limit[1]])
            if left == False or right == False :
                return False
            return left and right
        return check(root , [float('-infinity') , float('infinity')])







        
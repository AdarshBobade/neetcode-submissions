# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checksametree(root1 , root2):
            if root1 is None and root2 is None :
                return True
            if root1 is None or root2 is None or (root1.val != root2.val) :
                return False
            return checksametree(root1.left , root2.left) and checksametree(root1.right , root2.right)

        def traversal(root1 , root2) :
            if root1 is None :
                return False
            if root1.val == root2.val :
                if checksametree(root1 , root2):
                    return True
            return traversal(root1.left , root2) or traversal(root1.right , root2)


        return traversal(root , subRoot)

            
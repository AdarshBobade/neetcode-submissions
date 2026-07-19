# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None :
            return None
        if root.val == key:
            self.deletion(root)
        
        tmp = root
        while tmp is not None:
            if tmp.val > key :
                if tmp.left and tmp.left.val == key :
                    tmp.left = self.deletion(tmp.left)
                    break
                else :
                    tmp = tmp.left
            
            else :
                if tmp.right and tmp.right.val == key :
                    tmp.right = self.deletion(tmp.right)
                    break
                else :
                    tmp = tmp.right
        return root
    def deletion(self , tmp):
        if tmp.left is None :
            return tmp.right
        elif tmp.right is None :
            return tmp.left
        else :
            right_child = tmp.right
            last_right = self.findlastnode(tmp.left)
            last_right.right = right_child
            return tmp.left

    
    def findlastnode(self, node):
        while node.right is not None:
            node = node.right
        return node








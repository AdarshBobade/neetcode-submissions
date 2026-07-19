# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def search(node , target):
            prev = None
            cur = node 
            while cur is not None:
                if cur.val == target :
                    return prev , cur
                elif cur.val > target :
                    prev = cur
                    cur = cur.left
                else :
                    prev = cur
                    cur = cur.right
            return None
        
        prev , tmp = search(root , key)

        if prev.left == tmp :
            left_node = tmp.left
            right_node = tmp.right
            if left_node :
                prev.left = left_node
                left_node.right = right_node

            elif right_node :
                prev.left = right_node
                right_node.left = left_node

            else :
                prev.left = None
        
        elif prev.right == tmp :
            left_node = tmp.left
            right_node = tmp.right

            if tmp.left :
                prev.right = left_node
                left_node.right = right_node
            elif tmp.right :
                prev.right = right_node
                right_node.left = left_node
                
            else :
                prev.right = None

        return root








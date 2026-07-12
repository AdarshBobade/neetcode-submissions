# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res , stack = [] , []
        cur = root
        while cur is not None or stack :
            if cur is not None :
                stack.append(cur)
                cur = cur.left
            elif cur is None :
                temp = stack[-1].right
                if temp is None:
                    temp = stack.pop()
                    res.append(temp.val)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        res.append(temp.val)
                else :
                    cur = temp
        
        return res

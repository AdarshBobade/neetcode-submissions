# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root :
            return res
        q1 = deque([root])
        while q1 :
            level = []
            qLen = len(q1)
            for _ in range(qLen):
                node = q1.popleft()
                level.append(node.val)
                if node.left :
                    q1.append(node.left)
                if node.right :
                    q1.append(node.right)
            
            if (len(res) + 1 ) % 2 == 0:
                res.append(level[::-1])
            else :
                res.append(level)
        
        return res
            










        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q1 = deque([root])
        if not root :
            return res
        while q1 :
            rightSide = None
            qLen = len(q1)
            for _ in range(qLen):
                node = q1.popleft()
                if node :
                    rightSide = node
                    q1.append(node.left)
                    q1.append(node.right)
            
            if rightSide :
                res.append(rightSide.val)
        return res

                








